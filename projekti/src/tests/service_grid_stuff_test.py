import unittest
from entities.user import User
from entities.board import Board
from repositories.user_repository import user_test_repository
from repositories.grid_repository import grid_test_repository
from initialize_database import initialize_test_database
from services import GOLService


class TestLoginRegister(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.user1 = User("Gail", "Gail")
        self.board1 = Board(3, "board1")
        self.service = GOLService(grid_test_repository, user_test_repository)

    def test_create_board_service(self):
        self.service.create_board("3x3", "test1")
        board = self.service.board()
        board_name = board._name
        board_data = board._grid
        self.assertEqual(
            (board_name, str(board_data)),
            ("test1", str([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        )

    def test_save_board_service(self):
        self.service.create_board("3x3", "test1")
        self.service.save_board()
        board = self.service.board()
        board_name = board._name
        board_data = board._grid
        self.assertEqual(
            (board_name, str(board_data)),
            ("test1", str([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        )

    def test_load_board_service(self):
        self.service.create_board("3x3", "test1")
        self.service.save_board()
        self.service.create_board("3x3", "test2")
        self.service.save_board()
        self.service.load_board(1)
        board = self.service.board()
        board_name = board._name
        board_data = board._grid
        self.assertEqual(
            (board_name, str(board_data)),
            ("test1", str([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        )

    def test_manipulate_board_service(self):
        self.service.create_board("3x3", "test1")
        self.service.manipulate_board(1, 1)
        board = self.service.board()
        board_name = board._name
        board_data = board._grid
        self.assertEqual(
            (board_name, str(board_data)),
            ("test1", str([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
        )

    def test_step_board_service(self):
        self.service.create_board("3x3", "test1")
        self.service.manipulate_board(1, 1)
        self.service.step_board()
        board = self.service.board()
        board_name = board._name
        board_data = board._grid
        self.assertEqual(
            (board_name, str(board_data)),
            ("test1", str([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        )

    def test_get_all_boards(self):
        self.service.create_board("3x3", "test1")
        self.service.save_board()
        self.service.create_board("3x3", "test2")
        self.service.save_board()
        boards = self.service.get_boards()
        self.assertEqual(
            len(boards),
            2
        )

    def test_create_board_service_empty_input(self):
        with self.assertRaises(Exception):
            self.service.create_board("", "test1")
        with self.assertRaises(Exception):
            self.service.create_board("3x3", "")

    def test_create_board_service_board_exists(self):
        self.service.create_board("3x3", "test1")
        self.service.save_board()
        with self.assertRaises(Exception):
            self.service.create_board("3x3", "test1")
