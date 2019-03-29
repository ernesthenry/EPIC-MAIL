from flask import Blueprint, request
from api.controllers.group_controllers import GroupController
from flask_jwt_extended import get_jwt_identity, jwt_required


group_blueprint = Blueprint("group_blueprint", __name__)
group_controller = GroupController()


@group_blueprint.route("/groups", methods=["POST"])
@jwt_required
def create_group(user):
    current_user = get_jwt_identity()
    data = request.get_json()
    return group_controller.new_group(data)


@group_blueprint.route('/groups/<int:group_id>', methods=['DELETE'])
@jwt_required
def delete_group(group_id):
    """ delete a specific  group """
    return group_controller.delete_group(group_id)


@group_blueprint.route("/groups", methods=["GET"])
@jwt_required
def all_groups():
    """Get all groups"""
    return group_controller.fetch_all_groups()


@group_blueprint.route('/groups/<int:group_id>/name', methods=['PATCH'])
@jwt_required
def change_group_name(group_id):
    "Edit group name """
    data = request.get_json()
    return group_controller.edit_group_name(group_id, data["group_name"])


@group_blueprint.route("/groups/<int:group_id>", methods=["GET"])
@jwt_required
def single_group(group_id):
    """Get a specific group"""
    return group_controller.fetch_single_group(group_id)
