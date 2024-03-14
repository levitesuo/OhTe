import unittest
from entities.user import User
from repositories.user_repository import user_test_repository
from repositories.grid_repository import grid_test_repository
from initialize_database import initialize_test_database
from services import GOLService


class TestLoginRegister(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self.user1 = User("Gail", "Gail")
        self.user2 = User("Jack", "Jack")
        self.service = GOLService(grid_test_repository, user_test_repository)
        self.service.register_user(self.user2.username, self.user2.password)
        self.service.logout()

    def test_register_user_service(self):
        self.service.register_user(self.user1.username, self.user1.password)
        user_from_db = user_test_repository.find_by_username(
            self.user1.username)
        self.assertEqual(self.user1.get_user_info(),
                         user_from_db.get_user_info())

    def test_login_user_service(self):
        self.service.login(self.user2.username, self.user2.password)
        self.assertEqual(self.user2.get_user_info(),
                         self.service.user().get_user_info())
