import json
from entities.board import Board
from database_connection import get_database_connection, get_test_connection


class GridRepository:
    '''
    A class to enable the saving and fetching of grids from the database.

    ...

    Attributes
    ----------
    _connection : Connection
        a connection to the database

    Methods
    -------
    save_grid(grid: Board, user_id)
        Saves a grid to the database with the given user_id.

    get_grid_by_id(grid_id)
        Fetches a grid from the database by its id.

    get_grid_by_name(grid_name)
        Fetches a grid from the database by its name.

    get_all()
        Fetches all grids from the database.
    '''

    def __init__(self, connection):
        '''
        Constructs all the necessary attributes for the grid repository object.

        Parameters
        ----------
        connection : Connection
            a connection to the database
        '''
        self._connection = connection

    def save_grid(self, grid: Board, user_id):
        '''
        Saves a grid to the database with the given user_id.

        Parameters
        ----------
        grid : Board
            the grid to be saved

        user_id : int
            the id of the user who is saving the grid
        '''
        cursor = self._connection.cursor()
        grid = grid.get_grid()

        if self.get_grid_by_id(grid_id=grid['grid_id']):
            grid['name'] = grid['name'] + " COPY"

        content = str(grid["grid"])
        cursor.execute("INSERT INTO grids (name, content, owner_id) values (?, ?, ?)",
                       (grid["name"], content, user_id))
        self._connection.commit()

    def get_grid_by_id(self, grid_id):
        '''
        Fetches a grid from the database by its id.

        Parameters
        ----------
        grid_id : int
            the id of the grid to be fetched

        Returns
        -------
        Board
            the grid fetched from the database as a board object
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM grids WHERE grids.grid_id = ?",
                       (grid_id,))

        grid_info = cursor.fetchone()
        if not grid_info:
            return None
        grid = json.loads(grid_info["content"])
        size = len(grid)
        new_board = Board(size, grid_info["name"], grid_info["grid_id"], grid)
        return new_board

    def get_grid_by_name(self, grid_name):
        '''
        Fetches a grid from the database by its name.

        Parameters
        ----------
        grid_name : str
            the name of the grid to be fetched

        Returns
        -------
        Board
            the grid fetched from the database as a board object
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM grids WHERE grids.name = ?",
                       (grid_name,))

        grid_info = cursor.fetchone()
        if not grid_info:
            return None
        grid = json.loads(grid_info["content"])
        size = len(grid)
        new_board = Board(size, grid_info["name"], grid_info["grid_id"], grid)
        return new_board

    def get_all(self):
        '''
        Fetches all grids from the database.

        Returns
        -------
        list
            a list of all grids fetched from the database as board objects
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM grids;")

        grid_infos = cursor.fetchall()

        grids = []

        for g in grid_infos:
            grid = json.loads(g["content"])
            size = len(grid)
            new_board = Board(size, g["name"], g["grid_id"], grid)
            grids.append(new_board)

        return grids


grid_repository = GridRepository(get_database_connection())
grid_test_repository = GridRepository(get_test_connection())
