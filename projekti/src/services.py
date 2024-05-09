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


class EmptyInputError(Exception):
    pass


class BoardExistsError(Exception):
    pass


class GOLService:
    '''
    A class to handle the game of life logic and user interaction.

    ...
    Attributes
    ----------
    _user : User
        the user currently logged in

    _board : Board
        the board currently loaded in

    _grid_repository : GridRepository
        the repository for the grids

    _user_repository : UserRepository
        the repository for the users

    Methods
    -------
    register_user(username, password)
        Registers a new user with the given username and password. 
        Raises an error if the username already exists.

    login(username, password)
        Logs in a user with the given username and password. 
        Raises an error if the username or password is incorrect.

    logout()
        Logs out the current user. Logs in the guest user.

    create_board(size, name)
        Creates a new board with the given size and name.

    save_board()
        Saves the current board to the database.

    load_board(board_id)
        Loads a board from the database with the given id.

    get_boards()
        Fetches all the boards from the database.

    manipulate_board(x, y)
        Changes the value of the cell at (x, y) to the opposite.

    step_board()
        Steps the board once.

    user()
        Returns the current user.

    board()
        Returns the current board.
    '''

    def __init__(
        self,
        grid_repository=default_grid_repository,
        user_repository=default_user_repository,

    ):
        self._user = None
        self._board = None
        self._grid_repository = grid_repository
        self._user_repository = user_repository
        self.login("Guest", "Guest")

    def register_user(self, username, password):
        '''
        Registers a new user with the given username and password. 
        Raises an error if the username already exists.

        Parameters
        ----------
        username : str
            the username of the new user

        password : str
            the password of the new user

        Raises
        ------
        UsernameExistsError
            if the username already exists
        '''
        if not username or not password:
            raise EmptyInputError("Username and password must not be empty")

        user_exists = self._user_repository.find_by_username(username)
        if user_exists is not None:
            raise UsernameExistsError(f"Username {username} already exists")
        user = User(username, password)
        self._user_repository.register_user(user)
        self._user = user

    def login(self, username, password):
        '''
        Logs in a user with the given username and password. 
        Raises an error if the username or password is incorrect.

        Parameters
        ----------
        username : str
            the username of the user to be logged in

        password : str
            the password of the user to be logged in

        Raises
        ------ 
        InvalidCredentialsError
            if the username or password is incorrect
        '''
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user

    def logout(self):
        '''
        logs out the current user. Logs in the guest user.
        '''
        self.login("Guest", "Guest")

    def create_board(self, size, name):
        '''
        Creates a new board with the given size and name.

        Parameters
        ----------
        size : str
            the size of the board in the format "XxY" where X and Y are integers

        name : str
            the name of the board
        '''
        if not size or not name:
            raise EmptyInputError("Size and name must not be empty")
        board = self._grid_repository.get_grid_by_name(name)
        if board:
            raise BoardExistsError(f"Board with name {name} already exists")
        self._board = Board(int(size.split("x")[0]), name)

    def save_board(self):
        '''
        saves the current board to the database.
        '''
        self._grid_repository.save_grid(self._board, self._user.user_id)

    def load_board(self, board_id):
        '''
        loads a board from the database with the given id to self._board.
        '''
        self._board = self._grid_repository.get_grid_by_id(board_id)

    def get_boards(self):
        '''
        fetches all the boards from the database.

        Returns
        -------
        list
            a list containing all the boards as Board objects   
        '''
        return self._grid_repository.get_all()

    def manipulate_board(self, x, y):
        '''
        Manipulates the board by changing the value of the cell at (x, y) to the opposite.
        '''
        self._board.manipulate(x, y)

    def step_board(self):
        '''
        steps the board once.
        '''
        self._board.step()

    def user(self):
        '''
        Returns the current user.
        '''
        return self._user

    def board(self):
        '''
        Returns the current board.
        '''
        return self._board


gol_service = GOLService()
