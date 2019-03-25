import re

def user_validation(**kwargs):
    """Function that performs Validation of a user registering"""
    error = {}
    error["email"] = validate_email(kwargs["email"])
    error["firstname"] = validate_name(kwargs["firstname"])
    error["lastname"] = validate_name(kwargs["lastname"])
    error["password"] = validate_password(kwargs["password"])

    invalid = {key: value for key, value in error.items() if value}
    return invalid

def validate_email(email):
    """Function that performs Validation of a users email"""
    error = None
    if not email:
        error = "Email cant be left blank"
    elif not re.search(r'[^@]+@[^@]+\.[^@]+', email):
        error = "Wrong format for email"
    return error

def validate_name(name):
    """Function that performs Validation of a user's name"""
    if not name:
        return "Name should not be empty"

    if not isinstance(name, str):
        return "Name should be a string"

    for char in name:
        if char.isdigit():
            return "Name should not contain any integers"

    return None

def validate_password(password):
    """Function that performs Validation of a users password"""
    error = None
    if len(str(password)) <= 8:
        error = "Password should have greater than eight characters"
    elif not isinstance(password, str):
        error = "Password should  be a string"
    elif not re.search("[A-Z]", password)\
            or not re.search("[0-9]", password)\
            or not re.search("[a-z]", password)\
            or not re.search("[@$!%*?&#-]", password):
        error = "Password should have atleast one lowercase character,one Uppercase character, one Integer and one Special character"
    return error