import json
from entities.board import Board
from database_connection import get_database_connection, get_test_connection


class GridRepository:
    def __init__(self, connection):
        self._connection = connection

    def save_grid(self, grid: Board, user_id):
        cursor = self._connection.cursor()
        grid = grid.get_grid()
        content = str(grid["grid"])
        cursor.execute("INSERT INTO grids (grid_id, name, content, owner_id) values (?, ?, ?, ?)",
                       (grid["grid_id"], grid["name"], content, user_id))
        self._connection.commit()

    def get_grid_by_id(self, grid_id):
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
