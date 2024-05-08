# Calls a function when pressed
# Has different colors based on toggle state
import pygame


class Button:
    '''
    A class for easy creation of pygame buttons.

    ...
    Attributes
    ----------
    _screen : Surface
        the screen where the button is drawn

    _pos : tuple
        the position of the button on the screen

    _rect : Rect
        the rectangle object of the button

    _color : tuple
        the color of the button

    _text : str
        the text displayed on the button

    Methods
    -------
    set_color(color)
        Sets the color of the button.

    set_text(text)
        Sets the text of the button.

    draw()
        Draws the button on the screen.

    is_pressed(pos)
        Checks if the pos is inside the button.
    '''
    # Tämän luokan kirjoittamiseen on käytety apuna copilottia

    def __init__(self, screen, position, width, height, color, text):
        self._screen = screen
        self._pos = position
        self._rect = pygame.Rect(position[0], position[1], width, height)
        self._color = color
        self._text = text

    def set_color(self, color):
        '''
        Sets the color of the button.

        Parameters
        ----------
        color : tuple
            the color of the button as a tuple and in a format that pygame recognizes
        '''
        self._color = color

    def set_text(self, text):
        '''
        Sets the text of the button.

        Parameters
        ----------
        text : str
            the text displayed on the button
        '''
        self._text = text

    def draw(self):
        '''
        Draws the button on the screen.
        '''
        pygame.draw.rect(self._screen, self._color, self._rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self._text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self._rect.center)
        self._screen.blit(text, text_rect)

    def is_pressed(self, pos):
        '''
        Checks if the pos is inside the button.

        Parameters
        ----------
        pos : tuple
            the position of the mouse pointer

        Returns
        -------
        bool
            True if the pos is inside the button, False otherwise
        '''
        return self._rect.collidepoint(pos)
