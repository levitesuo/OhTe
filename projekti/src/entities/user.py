import uuid


class User:
    def __init__(self, name, password, user_id=uuid.uuid4()):
        self.user_id = str(user_id)
        self.username = name
        self.password = password
