import math
import pygame
from services import gol_service


class Engine:
    def __init__(self):
        self._speed = 0
        self._pause = True
        self._screen = None
        self._screen_size = (600, 600)
        self._mouse_pos = None
        self._cell_size = None
        self._offsets = None

    def start(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption(gol_service.board().get_grid()["name"])
        self._loop()

    def _loop(self):
        while True:
            self._mouse_pos = pygame.mouse.get_pos()
            self._screen.fill((100, 100, 100))
            self._check_events()
            self._render_grid()
            pygame.display.update()

    def _check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gol_service.step_board()

    def _handle_click(self):
        x = (self._mouse_pos[0] - self._offsets[0]) // self._cell_size
        y = (self._mouse_pos[1] - self._offsets[1]) // self._cell_size

        gol_service.manipulate_board(x, y)

    def _render_grid(self):
        grid_y_offset = 50
        grid_x_offset = 10
        self._offsets = (grid_x_offset, grid_y_offset)
        grid = gol_service.board().get_grid()
        grid_data = grid["grid"]
        grid_size = len(grid_data)
        self._cell_size = min(
            (self._screen_size[0] - grid_x_offset),
            (self._screen_size[1] - grid_y_offset)) // grid_size
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
                    [x * (self._cell_size) + grid_x_offset,
                     y * (self._cell_size) + grid_y_offset,
                     (self._cell_size - gap_size),
                     (self._cell_size - gap_size)]
                )


game_engine = Engine()
