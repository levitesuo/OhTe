from ui.menu_view import MenuView
from ui.board_creator_view import BoardCreatorView
from ui.login_view import LoginView
from ui.register_view import RegisterView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()

    def _show_main_menu(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = MenuView(
            self._root,
            self._show_board_maker_view,
            self._show_saved_view,
            self._show_login_view)
        self._current_view.pack()

    def _show_board_maker_view(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = BoardCreatorView(
            self._root,
            self._show_main_menu,
            self._show_main_menu
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

    def _show_saved_view(self):
        pass
