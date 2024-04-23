from entities.board import Board
from entities.user import User

from repositories.grid_repository import (
    grid_repository as default_grid_repository)

from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class GOLService:
    def __init__(
        self,
        grid_repository=default_grid_repository,
        user_repository=default_user_repository,

    ):
        self._user = None
        self._board = None
        self._grid_repository = grid_repository
        self._user_repository = user_repository
        if self._user is None:
            self.login("Guest", "Guest")

    def register_user(self, username, password):
        user_exists = self._user_repository.find_by_username(username)
        if not (user_exists is None):
            raise UsernameExistsError(f"Username {username} already exists")
        user = User(username, password)
        self._user_repository.register_user(user)
        self._user = user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user

    def logout(self):
        self.login("Guest", "Guest")

    def create_board(self, size, name):
        self._board = Board(int(size.split("x")[0]), name)

    def save_board(self):
        self._grid_repository.save_grid(self._board, self._user.user_id)

    def load_board(self, board_id):
        self._board = self._grid_repository.get_grid_by_id(board_id)

    def get_boards(self):
        return self._grid_repository.get_all()

    def manipulate_board(self, x, y):
        self._board.manipulate(x, y)

    def step_board(self):
        self._board.step()

    def user(self):
        return self._user

    def board(self):
        return self._board


gol_service = GOLService()
