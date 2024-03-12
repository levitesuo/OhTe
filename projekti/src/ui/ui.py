from ui.menu_view import MenuView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()

    def _show_main_menu(self):
        self._current_view = MenuView(
            self._root,
            self._show_board_view,
            self._show_saved_view,
            self._show_login_view)
        self._current_view.pack()

    def _show_board_view(self):
        pass

    def _show_login_view(self):
        pass

    def _show_saved_view(self):
        pass
