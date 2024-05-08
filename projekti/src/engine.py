import pygame
import pygame_widgets
from game_objects.button import Button
from game_objects.speed_slider import SpeedSlider
from services import gol_service


class Engine:
    '''
    A class for the game engine and pygame visualization.

    Attributes
    ----------
    _clock : Clock
        the clock object for the game

    _speed : int
        the speed of the game

    _counter : int
        a counter for the speed of the game

    _pause : bool
        a boolean for the pause state of the game

    _screen : Surface
        the screen of the game

    _screen_size : Vector2
        the size of the screen

    _mouse_pos : Vector2
        the position of the mouse

    _cell_size : int
        the size of the cells in the grid

    _offsets : Vector2
        the offsets for the grid rendering

    _zoom_scale : float
        the scale of the zoom

    _int_surf_size : Vector2
        the size of the internal surface

    _int_surf : Surface
        the internal surface for rendering

    _int_offset : Vector2
        the offset for the internal surface

    _slider : SpeedSlider
        the speed slider object

    _pause_button : Button
        the pause button object

    _step_button : Button
        the step button object

    _menu_button : Button
        the menu button object

    _save_button : Button
        the save button object

    Methods
    -------
    start()
        Starts the game engine.

    _init_screen()
        Initializes the screen, buttons and sliders.

    _loop()
        The main loop of the game.

    _speed_handler()
        Handles the speed of the game.

    _check_events(events)
        Checks the events for the game.

    _handle_click()
        Handles the click events.

    _toggle_pause()
        Toggles the pause state of the game.

    _offset_handler()
        Handles the offsets of the grid.

    _limit_offset(limit)
        Limits the offset of the grid.

    _render_grid()
        Renders the grid.
    '''

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
        self._pause_button = None
        self._step_button = None
        self._menu_button = None
        self._save_button = None

    def start(self):
        '''
        Starts the game engine.
        '''
        pygame.init()
        self._pause = True
        self._clock = pygame.time.Clock()
        self._init_screen()
        self._loop()

    def _init_screen(self):
        self._screen = pygame.display.set_mode(
            (self._screen_size.x, self._screen_size.y)
        )
        pygame.display.set_caption(gol_service.board().get_grid()["name"])

        self._slider = SpeedSlider(self._screen)
        self._pause_button = Button(
            self._screen,
            (40,
             self._screen_size.y - 60),
            100,
            50,
            (200, 100, 100),
            "Start",
        )
        self._step_button = Button(
            self._screen,
            (self._screen_size.x - 140,
             self._screen_size.y - 60),
            100,
            50,
            (100, 100, 200),
            "Step",
        )
        self._menu_button = Button(
            self._screen,
            (40,
             10),
            100,
            50,
            (100, 50, 150),
            "Menu",
        )
        self._save_button = Button(
            self._screen,
            (self._screen_size.x - 140,
             10),
            100,
            50,
            (100, 50, 150),
            "Save",
        )

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
            self._pause_button.draw()
            self._step_button.draw()
            self._menu_button.draw()
            self._save_button.draw()
            pygame.display.update()
            self._clock.tick(60)

    def _speed_handler(self):
        # Tämän funktion kirjoittamiseen käytetty apuna copilottia
        self._speed = self._slider.get_value()
        if not self._pause:
            if self._counter >= (100 - self._speed):
                self._counter = 0
                gol_service.step_board()
            else:
                self._counter += 1

    def _check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Right click
                    self._handle_click()
                elif event.button == 4:  # Mwheel up
                    self._zoom_scale += 0.1
                elif event.button == 5:  # Mwheel down
                    self._zoom_scale -= 0.1
                self._zoom_scale = max(0.1, self._zoom_scale)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._toggle_pause()

    def _handle_click(self):
        # Tämän function kirjoittamisessa on käytetty apuna copilottia
        if self._pause_button.is_pressed(self._mouse_pos):
            self._toggle_pause()
            return
        if self._step_button.is_pressed(self._mouse_pos):
            gol_service.step_board()
            return
        if self._menu_button.is_pressed(self._mouse_pos):
            pygame.quit()
            return
        if self._save_button.is_pressed(self._mouse_pos):
            gol_service.save_board()
            return
        if self._slider.contains(self._mouse_pos):
            return
        scaled_mouse_pos = (self._mouse_pos - self._screen_size / 2) / \
            self._zoom_scale + self._screen_size / 2
        grid = gol_service.board().get_grid()
        grid_size = len(grid["grid"])
        cell_size = self._cell_size
        x = int((scaled_mouse_pos.x - self._offsets.x) // cell_size)
        y = int((scaled_mouse_pos.y - self._offsets.y) // cell_size)
        if 0 <= x < grid_size and 0 <= y < grid_size:
            gol_service.manipulate_board(x, y)

    def _toggle_pause(self):
        self._pause = not self._pause
        if self._pause:
            self._pause_button.set_text("Start")
            self._pause_button.set_color((200, 100, 100))
        else:
            self._pause_button.set_text("Pause")
            self._pause_button.set_color((100, 200, 100))

    def _offset_handler(self):
        moving_speed = max(1 / self._zoom_scale, 0.1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self._offsets.x += moving_speed
        if keys[pygame.K_d]:
            self._offsets.x -= moving_speed
        if keys[pygame.K_s]:
            self._offsets.y -= moving_speed
        if keys[pygame.K_w]:
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
        gap_size = max(self._cell_size // 10, 1)
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


game_engine = Engine()
