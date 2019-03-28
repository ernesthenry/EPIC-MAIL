from flask import jsonify, request, json
from api.utilities.validation import validate_group
from api.controllers.user_controller import db
from api.utilities.helpers import get_current_identity


class GroupController():
    def new_group(self, data):
        if not request.data:
            return (
                jsonify(
                    {
                        "error": "Invalid request",
                        "   status": 400,
                    }
                ),
                400,
            )
        data = request.get_json(force=True)
        new_group = {
            "group_name": data.get("group_name"),
            "role": data.get("role")
        }

        group_name = data.get("group_name")
        # user_id =get_current_identity()

        invalid_group = validate_group(**new_group)
        if invalid_group:
            return jsonify({
                "status": 400,
                "Message": invalid_group
            }), 400
        if db.check_duplicate_group(group_name):
            return jsonify({
                "Message": "Group arleady exists",
                "status": 400
            }), 400

        group = db.create_group(**new_group)
        if group:
            return jsonify({
                "status": 201,
                "data": [{
                    "message": "Group created successfully"
                }]
            }), 201
        else:
            return jsonify({
                "status": 409,
                "error": "The group already exists"
            }), 409


    def fetch_single_group(self, group_id):
        single_group = db.get_specific_group(group_id)
        if single_group:
            return jsonify(
                {"status": 200,
                 "data": single_group
                 }), 200
        else:
            return jsonify(
                {
                    "status": 404,
                    "error": "Invalid request"
                }), 404


    def fetch_all_groups(self):
        """ Get all groups. """
        # login_credentials = json.loads(request.data)
        # get_user = get_current_identity()
        # group_id = get_user.get(login_credentials)
        groups = db.get_all_groups()
        if groups:
            return jsonify({
                "data": [group for group in groups],
                "status": 200
            }), 200

        return jsonify({
            "status": 404,
            "error": "No user groups yet."
        }), 404
