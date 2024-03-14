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
