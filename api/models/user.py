from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """ model class for users """

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.firstname = kwargs["firstname"]
        self.lastname = kwargs["lastname"]
        self.password = generate_password_hash(kwargs["password"])

    def format_user_record(self):
        return {
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password
        }
