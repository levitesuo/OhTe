from entities.user import User
from database_connection import get_database_connection, get_test_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def register_user(self, user: User):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (user_id, username, password) values (?, ?, ?)",
                       (user.user_id, user.username, user.password)
                       )
        self._connection.commit()

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE users.username = ?",
                       (username,))

        user_info = cursor.fetchone()

        if user_info:
            return User(user_info["username"], user_info["password"], user_info["user_id"])
        return None


user_repository = UserRepository(get_database_connection())
user_test_repository = UserRepository(get_test_connection())
