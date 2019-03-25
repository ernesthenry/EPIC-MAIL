#api/controllers
from flask import jsonify, request,json
from api.models.user import user_data, User, valid_credentials
from api.utilities.validation import user_validation
from api.utilities.helpers import generate_token

class UserController:
    def signup_user(self):
        data = json.loads(request.data)
        if not data:
            return jsonify(
                {
                    "status": 400,
                    "error": "Empty Registration request. Please provide Registration data"
                    }), 400
        new_user ={
            "email": data.get("email"),
            "firstname": data.get("firstname"),
            "lastname": data.get("lastname"),
            "password": data.get("password")
            }
        email = data.get("email")
        firstname = data.get("firstname")
        already_user = [user for user in user_data if user['email'] ==
        email
        ]
        if already_user:
            return jsonify({"status": 409, "error": "User already exists"}), 409
        not_valid_user = user_validation(**new_user)
        if not_valid_user:
            return jsonify({"status": 400, "error": not_valid_user}), 400
        user = User(**new_user)
        user_data.append(user.format_user_record())
        return jsonify({
            "status": 201,
            "data": [
                {
                    "user": user.format_user_record(),
                    "success": " User registered Successfully"}
                    ],
                }
                ),201


    def login_user(self):
        login_credentials = json.loads(request.data)
        response = None
        if not login_credentials:
            return jsonify(
                {
                    "status": 400,
                    "error": "Couldn't find your account"
            }), 400
        email = login_credentials.get("email")
        password = login_credentials.get("password")

        userid = valid_credentials(email,password)
        if userid:
            return  jsonify(
                        {
                            "status": 200,
                            "data": [
                                {
                                    "Token": generate_token(userid),
                                    "Success": "User logged in successfully"
                                }
                                ],
                                }
                                ),200
                            
        else:
            return jsonify({"error": "Wrong login credentials.", "status": 401}), 401
                       