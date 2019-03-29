from flask import jsonify, request, json
from api.utilities.validation import validate_group
from api.controllers.user_controller import db
from api.models.group import Group
from api.utilities.helpers import get_current_identity
from api.utilities.validation import validate_name


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
        return jsonify(
                {
                    "status": 404,
                    "error": "The record with such id does not exist"
                }), 404


    def fetch_all_groups(self):
        """ Get all groups. """
        groups = db.get_all_groups()
        return jsonify(groups)
    
    def delete_group(self, group_id):
        """delete a group """
        group_exists = db.group_exists(group_id)
        if group_exists is None:
            return jsonify({
                "error": "Can not delete a non existant endpoint.",
                "status": 404
            }), 404
            
        db.delete_group(group_id)
        return jsonify({
            "status": 200,
            "message": "Group successfully deleted."
        }), 200

    def edit_group_name(self, group_id,group_name):
        """
        Update group name.
        """
        group = db.update_group_name(group_id, group_name)

        if group is None:
            return jsonify({
                "error": "You can not update the name of a non existant group.",
                "status": 404
            }), 404

        new_group_name = request.get_json()

        name = new_group_name.get("group_name")

        invalid_name = validate_name(name)
        if invalid_name is False:
            return jsonify({
                "error": "Invalid new group name.",
                "status": 400
            }), 400

        return jsonify(group)
