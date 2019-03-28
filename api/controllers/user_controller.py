from flask import jsonify, request, json
from api.models.user import User, valid_credentials
from api.utilities.validation import user_validation
from api.utilities.helpers import generate_token
from werkzeug.security import check_password_hash
from api.db import DatabaseConnection

db = DatabaseConnection()


class UserController:
    def signup_user(self):
        data = json.loads(request.data)
        if not data:
            return jsonify(
                {
                    "status": 400,
                    "error": "Empty Registration request. Please provide Registration data"
                }), 400
        new_user = {
            "email": data.get("email"),
            "firstname": data.get("firstname"),
            "lastname": data.get("lastname"),
            "password": data.get("password")
        }
        email = data.get("email")
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        password = data.get("password")

        not_valid_user = user_validation(**new_user)
        if not_valid_user:
            return jsonify({"status": 400, "message": not_valid_user}), 400
        if db.check_email(email):
            return jsonify(
                {
                    "status": 409,
                    "error": "User already exists"
                }), 409
        user = db.register_user(email, firstname, lastname, password)
        return jsonify({
            "status": 201,
            "data": [
                {
                    "user": new_user,
                    "message": " User registered Successfully"}
            ],
        }
        ), 201

    def login_user(self):
        login_credentials = json.loads(request.data)
        if not login_credentials:
            return jsonify(
                {
                    "status": 400,
                    "error": "Couldn't find your account"
                }), 400

        email = login_credentials.get("email")
        password = login_credentials.get("password")
        user = db.login(email)
        if user is None:
            return jsonify({
                "status": 401,
                'error': 'User not found'
            }), 401
        elif user["email"] and check_password_hash(user["password"], password):
            return jsonify(
                {
                    "status": 200,
                    "data": [
                        {
                            "Token": generate_token(user["email"]),
                            "Success": "User logged in successfully"
                        }
                    ],
                }
            ), 200

        else:
            return jsonify({
                "error":
                "Wrong login credentials.",
                "status": 401
            }), 401
