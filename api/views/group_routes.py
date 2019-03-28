from flask import Blueprint, request
from api.controllers.group_controllers import GroupController
from api.utilities.helpers import token_required

group_blueprint = Blueprint("group_blueprint", __name__, url_prefix="/api/v1")


group_controller = GroupController()


@group_blueprint.route("/groups", methods=["POST"])
@token_required
def create_group():
    data = request.get_json()
    return group_controller.new_group(data)
