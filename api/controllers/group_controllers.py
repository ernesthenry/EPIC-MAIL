from flask import jsonify, request
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
        userid =get_current_identity()

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
                    "mail": group,
                    "message": "Group created successfully",
                }]
            }), 201
        else:
            return jsonify({
                "status": 409,
                "error": "The group already exists"
            }), 409
