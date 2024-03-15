import time
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from services import gol_service


class Engine:
    def __init__(self):
        self._clock = None
        self._speed = 0
        self._counter = 0
        self._pause = True
        self._screen = None
        self._screen_size = pygame.math.Vector2(600, 600)
        self._mouse_pos = None
        self._cell_size = None
        self._offsets = pygame.math.Vector2()

        self._zoom_scale = 0.5
        self._int_surf_size = pygame.math.Vector2(2000, 2000)
        self._int_surf = pygame.Surface(self._int_surf_size, pygame.SRCALPHA)
        self._int_offset = pygame.math.Vector2(
            self._int_surf_size // 2 - self._screen_size // 2)

        self._slider = None

    def start(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(
            (self._screen_size.x, self._screen_size.y)
        )
        pygame.display.set_caption(gol_service.board().get_grid()["name"])
        self._slider = self._speed_slider()
        self._loop()

    def _loop(self):
        while True:
            events = pygame.event.get()
            self._mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
            self._screen.fill((100, 100, 100))
            self._int_surf.fill((100, 100, 100))
            self._check_events(events)
            self._offset_handler()
            self._render_grid()
            pygame_widgets.update(events)
            self._speed_handler()
            pygame.display.update()
            self._clock.tick(60)

    def _speed_handler(self):
        # Tämän funktion kirjoittamiseen käytetty apuna copilottia
        self._speed = self._slider.getValue()
        if not self._pause:
            if self._counter >= (100 - self._speed):
                self._counter = 0
                gol_service.step_board()
            else:
                self._counter += 1

    def _check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Right click
                    self._handle_click()
                elif event.button == 4:  # Mwheel up
                    self._zoom_scale += 0.1
                elif event.button == 5:  # Mwheel down
                    self._zoom_scale -= 0.1
                self._zoom_scale = max(0.1, self._zoom_scale)

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self._key_handler(event)

    def _handle_click(self):
        # Tämän function kirjoittamisessa on käytetty apuna copilottia
        scaled_mouse_pos = (self._mouse_pos - self._screen_size / 2) / \
            self._zoom_scale + self._screen_size / 2
        grid = gol_service.board().get_grid()
        grid_size = len(grid["grid"])
        cell_size = self._cell_size
        x = int((scaled_mouse_pos.x - self._offsets.x) // cell_size)
        y = int((scaled_mouse_pos.y - self._offsets.y) // cell_size)
        if 0 <= x < grid_size and 0 <= y < grid_size:
            gol_service.manipulate_board(x, y)

    def _key_handler(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self._pause = not self._pause

    def _offset_handler(self):
        moving_speed = max(1 / self._zoom_scale, 0.1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._offsets.x += moving_speed
        if keys[pygame.K_RIGHT]:
            self._offsets.x -= moving_speed
        if keys[pygame.K_DOWN]:
            self._offsets.y -= moving_speed
        if keys[pygame.K_UP]:
            self._offsets.y += moving_speed

        offset_limit = self._int_surf_size / 2 - self._screen_size / 2
        self._limit_offset(offset_limit)

    def _limit_offset(self, limit):
        self._offsets.x = max(-limit.x, min(limit.x, self._offsets.x))
        self._offsets.y = max(-limit.y, min(limit.y, self._offsets.y))

    def _render_grid(self):
        grid = gol_service.board().get_grid()
        grid_data = grid["grid"]
        grid_size = len(grid_data)
        self._cell_size = self._screen_size.x // grid_size
        gap_size = min(self._cell_size // 10, 1)
        for x in range(grid_size):
            for y in range(grid_size):
                cell = grid_data[y][x]
                if cell:
                    color = (200, 200, 200)
                else:
                    color = (50, 50, 50)
                pygame.draw.rect(
                    self._int_surf,
                    color,
                    [x * (self._cell_size) + self._offsets.x + self._int_offset.x,
                     y * (self._cell_size) +
                     self._offsets.y + self._int_offset.y,
                     (self._cell_size - gap_size),
                     (self._cell_size - gap_size)]
                )

        scaled_surf = pygame.transform.scale(
            self._int_surf, self._int_surf_size * self._zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=self._screen_size / 2)
        self._screen.blit(scaled_surf, scaled_rect)

    def _speed_slider(self):
        # Tämän function kirjoittamisessa on käytetty apuna copilottia
        slider = Slider(
            self._screen,
            int(self._screen_size.x // 2 - 100),
            int(self._screen_size.y - 50),
            200,
            20,
            color=(10, 20, 70),
            handle_color=(20, 40, 140)
        )
        return slider


game_engine = Engine()
