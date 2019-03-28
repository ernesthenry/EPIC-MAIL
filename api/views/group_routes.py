from flask import Blueprint, request
from api.controllers.group_controllers import GroupController
from api.utilities.helpers import token_required
import time
group_blueprint = Blueprint("group_blueprint", __name__, url_prefix="/api/v1")


group_controller = GroupController()


@group_blueprint.route("/groups", methods=["POST"])
@token_required
def create_group(user):
    data = request.get_json()
    return group_controller.new_group(data)


@group_blueprint.route("/groups", methods=["GET"])
def all_groups():
    group_controller.fetch_all_groups()

@group_blueprint.route('/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """ 
    delete a group """
    return group_controller.delete_group(group_id)