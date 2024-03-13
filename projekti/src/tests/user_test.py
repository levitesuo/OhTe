import unittest
import uuid
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User('AndyU', 'AndyP')
        self.user2_id = uuid.uuid4()
        self.user2 = User('BillU', 'BillP', self.user2_id)

    def test_init_no_given_id(self):
        uid = self.user1.user_id
        self.assertEqual(
            {'user_id': uid, 'username': "AndyU", 'password': "AndyP"}, self.user1.get_user_info())

    def test_init_given_id(self):
        uid = str(self.user2_id)
        self.assertEqual(
            {'user_id': uid, 'username': "BillU", 'password': "BillP"}, self.user2.get_user_info())
