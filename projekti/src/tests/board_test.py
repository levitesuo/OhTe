import unittest
import uuid
from entities.board import Board


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, "test board")

    def test_to_string(self):
        s = "000\n000\n000\n"
        self.assertEqual(s, str(self.board))

    def test_load_grid(self):
        grid_id = uuid.uuid4
        grid = [[0]]
        name = "load test board"
        self.board.load_grid(grid, name, grid_id)
        self.assertEqual({"grid": grid, "name": name,
                         "grid_id": grid_id}, self.board.get_grid())

    def test_load_not_square(self):
        grid = [[0], [0]]
        grid_id = uuid.uuid4
        name = "load test board"
        self.assertEqual("ERROR: The grid must be a square.",
                         self.board.load_grid(grid, name, grid_id))

    def test_load_non_01(self):
        grid = [[5]]
        grid_id = uuid.uuid4
        name = "load test board"
        self.assertEqual("ERROR: The grid must contain only zeros and ones.",
                         self.board.load_grid(grid, name, grid_id))

    def test_manipulate_middle(self):
        self.board.manipulate(1, 1)
        right_grid = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])

    def test_manipulate_side(self):
        self.board.manipulate(2, 1)
        right_grid = [[0, 0, 0],
                      [0, 0, 1],
                      [0, 0, 0]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])

    def test_manipulate_full(self):
        self.board.manipulate(1, 1)
        self.board.manipulate(1, 1)
        right_grid = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])

    def test_step_empty(self):
        self.board.step()
        right_grid = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])

    def test_step_offspring(self):
        self.board.manipulate(0, 0)
        self.board.manipulate(1, 0)
        self.board.manipulate(1, 1)
        self.board.manipulate(2, 0)
        self.board.step()
        right_grid = [[1, 1, 1],
                      [1, 1, 1],
                      [0, 0, 0]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])

    def test_step_overpopulation(self):
        for i in range(3):
            for j in range(3):
                self.board.manipulate(i, j)
        self.board.step()
        right_grid = [[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]]
        self.assertEqual(right_grid, self.board.get_grid()["grid"])
