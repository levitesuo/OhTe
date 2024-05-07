import uuid


class User:
    '''
    A class to hold all the data for the user.

    Attributes
    ----------
    user_id : str
        the id of the user

    username : str
        the name of the user

    password : str
        the password of the user

    Methods
    -------
    get_user_info()
        Returns all the info about the user as a dictionary.
    '''

    def __init__(self, name, password, user_id=uuid.uuid4()):
        self.user_id = str(user_id)
        self.username = name
        self.password = password

    def get_user_info(self):
        '''
        Returns all the info about the user as a dictionary.

        Returns
        -------
        dict
            a dictionary containing all the info about the user
        '''
        return {'user_id': self.user_id, 'username': self.username, 'password': self.password}
