import unittest
from entities.user import User
from repositories.user_repository import user_test_repository
from repositories.grid_repository import grid_test_repository
from initialize_database import initialize_test_database
from services import GOLService


class TestLoginRegister(unittest):
    def setUp(self):
        initialize_test_database()
        self.user1 = User("Andy", "Andy")
        self.user2 = User("Bill", "Bill")
        self.service = GOLService(grid_test_repository, user_test_repository)
