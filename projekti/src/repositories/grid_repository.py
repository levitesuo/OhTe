from entities.board import Board
from database_connection import get_database_connection


class GridRepository:
    def __init__(self, connection):
        self._connection = connection

    def save_grid(self, grid: Board, user_id):
        cursor = self._connection.cursor()
        grid = grid.get_grid()
        content = str(grid["grid"])
        cursor.execute("INSERT INTO grids (grid_id, name, content, owner_id) values (? ? ? ?)",
                       (grid["grid_id"], grid["name"], content, user_id))

    def get_grid_by_id(self, grid_id):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM grids WHERE grids.grid_id = ?",
                       (grid_id,))

        grid_info = cursor.fetchone()
        grid = eval(grid_info["content"])
        size = len(grid)
        new_board = Board(size, grid_info["name"], grid_info["grid_id"], grid)
        return new_board


grid_repository = GridRepository(get_database_connection())
