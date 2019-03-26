
from flask import Blueprint, request
from api.controllers.message_controller import MessageController
from api.utilities.helpers import token_required

msg_controller = MessageController()

message_bp = Blueprint("message_bp", __name__)

@message_bp.route("/messages", methods = ["POST"])
# @token_required
def message():
    data = request.get_json(force=True)
    return msg_controller.new_message(data)