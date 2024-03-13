import unittest
from entities.user import User
from repositories.user_repository import user_test_repository
from initialize_database import initialize_test_database


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.user1 = User("Andy", "Andy")
        self.user2 = User("Bill", "Bill")
        user_test_repository.register_user(self.user1)
        user_test_repository.register_user(self.user2)

    def test_get_user_by_username(self):
        db_user = user_test_repository.find_by_username(self.user1.username)
        self.assertEqual(db_user.get_user_info(), self.user1.get_user_info())

    def test_fail_to_find(self):
        db_user = user_test_repository.find_by_username("Pasi")
        self.assertEqual(None, db_user)
