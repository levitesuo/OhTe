import unittest
from entities.board import Board
from entities.user import User
from repositories.grid_repository import grid_test_repository
from initialize_database import initialize_test_database


class TestGridRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.user1 = User("Andy", "Andy")
        self.user2 = User("Bill", "Bill")
        grid1 = [[1, 0, 1],
                 [0, 1, 0],
                 [1, 0, 1]]
        grid2 = [[1, 0, 0, 1],
                 [1, 0, 0, 1],
                 [1, 0, 0, 1]]
        self.board1 = Board(3, "x", grid_data=grid1)
        self.board2 = Board(5, "lines", grid_data=grid2)

        grid_test_repository.save_grid(self.board1, self.user1.user_id)
        grid_test_repository.save_grid(self.board2, self.user2.user_id)

    def test_get_board_by_id(self):
        grid_id = self.board1.get_grid()["grid_id"]
        board = grid_test_repository.get_grid_by_id(grid_id)
        self.assertEqual(self.board1.get_grid(), board.get_grid())

    def test_get_board_by_name(self):
        grid_name = self.board1.get_grid()["name"]
        board = grid_test_repository.get_grid_by_name(grid_name)
        self.assertEqual(self.board1.get_grid(), board.get_grid())

    def test_get_all_boards(self):
        db_boards_raw = grid_test_repository.get_all()
        db_boards = []
        for b in db_boards_raw:
            db_boards.append(b.get_grid())
        self.assertEqual(
            db_boards, [self.board1.get_grid(), self.board2.get_grid()])

    def test_fail_to_find(self):
        grid_id = "aaa"
        board = grid_test_repository.get_grid_by_id(grid_id)
        self.assertEqual(None, None)
