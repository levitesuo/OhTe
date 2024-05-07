from pygame_widgets.slider import Slider


class Speed_Slider:
    '''
    A class for easy creation of a speed slider from pygame_widgets

    ...
    Attributes
    ----------
    _slider : Slider
        the slider object

    Methods
    -------
    get_value()
        Returns the value of the slider.

    contains(pos)
        Checks if the pos is inside the slider.
    '''

    def __init__(self, screen):
        '''
        Constructs all the necessary attributes for the speed slider object.

        Parameters
        ----------
        screen : Surface
            the screen where the slider is drawn
        '''
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
        '''
        Returns the value of the slider.

        Returns
        -------
        int
            the value of the slider
        '''
        return self._slider.getValue()

    def contains(self, pos):
        '''
        Checks if the pos is inside the slider.

        Parameters
        ----------
        pos : tuple
            the position to be checked

        Returns
        -------
        bool
            True if the pos is inside the slider, False otherwise
        '''
        x = pos[0]
        y = pos[1]
        return self._slider.contains(x, y)
