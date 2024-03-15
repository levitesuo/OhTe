import pygame
from services import gol_service


class Engine:
    def __init__(self):
        self._speed = 0
        self._pause = True
        self._screen = None
        self._screen_size = pygame.math.Vector2(600, 600)
        self._mouse_pos = None
        self._cell_size = None
        self._offsets = pygame.math.Vector2(10, 50)
        self._moving = {"Right": False,
                        "Left": False, "Up": False, "Down": False}

    def start(self):
        pygame.init()
        self._screen = pygame.display.set_mode(
            (self._screen_size.x, self._screen_size.y)
        )
        pygame.display.set_caption(gol_service.board().get_grid()["name"])
        self._loop()

    def _loop(self):
        while True:
            self._mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
            self._screen.fill((100, 100, 100))
            self._check_events()
            self._offset_handler()
            self._render_grid()
            pygame.display.update()

    def _check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self._key_handler(event)

    def _handle_click(self):
        x = int((self._mouse_pos.x - self._offsets.x) // self._cell_size)
        y = int((self._mouse_pos.y - self._offsets.y) // self._cell_size)
        board_size = len(gol_service.board().get_grid()["grid"])
        if 0 <= x < board_size and 0 <= y < board_size:
            gol_service.manipulate_board(x, y)

    def _key_handler(self, event):
        arrow_keys = [pygame.K_RIGHT, pygame.K_LEFT,
                      pygame.K_UP, pygame.K_DOWN]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gol_service.step_board()
        if event.key in arrow_keys:
            self._arrowkey_handler(event)

    def _arrowkey_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._moving["Left"] = True
            if event.key == pygame.K_RIGHT:
                self._moving["Right"] = True
            if event.key == pygame.K_DOWN:
                self._moving["Down"] = True
            if event.key == pygame.K_UP:
                self._moving["Up"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self._moving["Left"] = False
            if event.key == pygame.K_RIGHT:
                self._moving["Right"] = False
            if event.key == pygame.K_DOWN:
                self._moving["Down"] = False
            if event.key == pygame.K_UP:
                self._moving["Up"] = False

    def _offset_handler(self):
        moving_speed = 1
        if self._moving["Left"]:
            self._offsets.x += moving_speed
        if self._moving["Right"]:
            self._offsets.x -= moving_speed
        if self._moving["Down"]:
            self._offsets.y -= moving_speed
        if self._moving["Up"]:
            self._offsets.y += moving_speed

        offset_limit = self._screen_size / 2
        self._limit_offset(offset_limit)

    def _limit_offset(self, limit):
        self._offsets.x = min(
            max(-limit.x, self._offsets.x), limit.x)

        self._offsets.y = min(
            max(-limit.y, self._offsets.y), limit.y)

    def _render_grid(self):
        grid = gol_service.board().get_grid()
        grid_data = grid["grid"]
        grid_size = len(grid_data)
        self._cell_size = self._screen_size.x // grid_size
        gap_size = max(self._cell_size // 10, 2)
        for x in range(grid_size):
            for y in range(grid_size):
                cell = grid_data[y][x]
                if cell:
                    color = (200, 200, 200)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(
                    self._screen,
                    color,
                    [x * (self._cell_size) + self._offsets.x,
                     y * (self._cell_size) + self._offsets.y,
                     (self._cell_size - gap_size),
                     (self._cell_size - gap_size)]
                )


game_engine = Engine()
