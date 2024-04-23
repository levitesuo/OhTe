from tkinter import Tk
from engine import game_engine

from ui.menu_view import MenuView
from ui.board_creator_view import BoardCreatorView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.load_view import LoadView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()

    def _restart(self):
        window = Tk()
        window.geometry('500x500')
        window.title("Game of life")
        self._root = window
        self._current_view = None
        self.start()
        window.mainloop()

    def _pygame_handler(self):
        self._root.destroy()
        try:
            game_engine.start()
        except:
            self._restart()

    def _show_main_menu(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = MenuView(
            self._root,
            self._show_board_maker_view,
            self._show_load_view,
            self._show_login_view,
            self._pygame_handler)
        self._current_view.pack()

    def _show_board_maker_view(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = BoardCreatorView(
            self._root,
            self._show_main_menu,
            self._show_main_menu,
            self._pygame_handler
        )
        self._current_view.pack()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = LoginView(
            self._root,
            self._show_main_menu,
            self._show_register_view,
            self._show_main_menu
        )
        self._current_view.pack()

    def _show_register_view(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = RegisterView(
            self._root,
            self._show_main_menu,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_load_view(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = LoadView(
            self._root,
            self._show_main_menu,
            self._pygame_handler
        )
