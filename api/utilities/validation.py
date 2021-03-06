import re


def user_validation(**kwargs):
    """Function that performs Validation of a user registering"""
    error = {}
    error["email"] = validate_email(kwargs["email"])
    error["email"] = contains_space(kwargs["email"])
    error["firstname"] = validate_name(kwargs["firstname"])
    error["lastname"] = validate_name(kwargs["lastname"])
    error["firstname"] = contains_space(kwargs["firstname"])
    error["lastname"] = contains_space(kwargs["lastname"])
    error["password"] = validate_password(kwargs["password"])
    error["password"] = contains_space(kwargs["password"])

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


def contains_space(input):
    """Checks if input contains a space"""
    error = None
    if " " in input or len(str(input).split(" ")) > 1:
        error = "Input should not contain any spaces"
    return error


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


def validate_message(**kwargs):
    errors = {}
    errors["subject"] = validate_sentence(kwargs.get("subject"))
    errors["message"] = validate_sentence(kwargs.get("message"))
    invalid = {key: value for key, value in errors.items() if value}
    return invalid


def validate_sentence(sentence):
    error = None
    sentence = str(sentence).strip()
    if sentence.isdigit():
        error = "Field cannot be a number"
    return error
