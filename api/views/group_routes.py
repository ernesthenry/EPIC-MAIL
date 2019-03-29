from flask import Blueprint, request
from api.controllers.group_controllers import GroupController
from api.utilities.helpers import token_required
import time
group_blueprint = Blueprint("group_blueprint", __name__)


group_controller = GroupController()


@group_blueprint.route("/groups", methods=["POST"])
@token_required
def create_group(user):
    data = request.get_json()
    return group_controller.new_group(data)

@group_blueprint.route('/groups/<int:group_id>', methods=['DELETE'])
@token_required
def delete_group(group_id):
    """ 
    delete a group """
    return group_controller.delete_group(group_id)


@group_blueprint.route("/groups", methods=["GET"])
def all_groups():
    return group_controller.fetch_all_groups()


@group_blueprint.route('/groups/<int:group_id>/name', methods=['PATCH'])
def change_group_name(group_id):
    "Edit group name """
    data = request.get_json()
    return group_controller.edit_group_name(group_id,data["group_name"])

@group_blueprint.route("/groups/<int:group_id>", methods=["GET"])
def single_group(group_id):
    return group_controller.fetch_single_group(group_id)

