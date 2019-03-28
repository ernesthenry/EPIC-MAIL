from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """ model class for users """

    def __init__(self, **kwargs):
        self.id = kwargs["-id"]
        self.email = kwargs["email"]
        self.firstname = kwargs["firstname"]
        self.lastname = kwargs["lastname"]
        self.password = generate_password_hash(kwargs["password"])

    def format_user_record(self):
        return {
            'id': self._id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password
        }


def valid_credentials(email, password):
    "checking for validity of user login details"
    for user in user_data:
        if user['email'] == email:
            return user

