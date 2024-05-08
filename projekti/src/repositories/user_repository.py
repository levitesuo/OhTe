from entities.user import User
from database_connection import get_database_connection, get_test_connection


class UserRepository:
    '''
    A class to enable the saving and fetching of users from the database.

    ...
    Attributes
    ----------
    _connection : Connection
        a connection to the database

    Methods
    -------
    register_user(user: User)
        Saves a user to the database.

    find_by_username(username)
        Fetches a user from the database by its username. Checks if the user exists.
    '''

    def __init__(self, connection):
        self._connection = connection

    def register_user(self, user: User):
        '''
        Saves a user to the database.

        Parameters
        ----------
        user : User
            the user to be saved as a User object
        '''
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (user_id, username, password) values (?, ?, ?)",
                       (user.user_id, user.username, user.password)
                       )
        self._connection.commit()

    def find_by_username(self, username):
        '''
        Fetches a user from the database by its username. Checks if the user exists.

        Parameters
        ----------
        username : str
            the username of the user to be fetched

        Returns
        -------
        User
            the user object fetched from the database as User object. 
            If the user does not exist, returns None.
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE users.username = ?",
                       (username,))

        user_info = cursor.fetchone()

        if user_info:
            return User(user_info["username"], user_info["password"], user_info["user_id"])
        return None


user_repository = UserRepository(get_database_connection())
user_test_repository = UserRepository(get_test_connection())
