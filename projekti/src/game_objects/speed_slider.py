from pygame_widgets.slider import Slider


class Speed_Slider:
    def __init__(self, screen):
        # Tämän function kirjoittamisessa on käytetty apuna copilottia
        screen_size = screen.get_size()
        self._slider = Slider(
            screen,
            int(screen_size[0] // 2 - 100),
            int(screen_size[1] - 50),
            200,
            20,
            color=(10, 20, 70),
            handle_color=(20, 40, 140),
            min=75
        )

    def get_value(self):
        return self._slider.getValue()

    def contains(self, pos):
        x = pos[0]
        y = pos[1]
        return self._slider.contains(x, y)
