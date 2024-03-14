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
        user_repository=default_user_repository
    ):
        self._user = None
        self._grid_repository = grid_repository
        self._user_repository = user_repository

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
        self._user = None

    def user(self):
        return self._user


gol_service = GOLService()
