# Calls a function when pressed
# Has different colors based on toggle state
import pygame


class Button:
    # Tämän luokan kirjoittamiseen on käytety apuna copilottia
    def __init__(self, screen, x, y, width, height, color, text):
        self._screen = screen
        self._pos = (x, y)
        self._rect = pygame.Rect(x, y, width, height)
        self._color = color
        self._text = text

    def set_color(self, color):
        self._color = color

    def set_text(self, text):
        self._text = text

    def draw(self):
        pygame.draw.rect(self._screen, self._color, self._rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self._text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self._rect.center)
        self._screen.blit(text, text_rect)

    def is_pressed(self, pos):
        return self._rect.collidepoint(pos)
