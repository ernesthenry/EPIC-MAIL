
from flask import Blueprint, request
from api.controllers.message_controller import MessageController
from api.utilities.helpers import token_required

msg_controller = MessageController()

message_bp = Blueprint("message_bp", __name__)

@message_bp.route("/messages", methods = ["POST"])
def message():
    data = request.get_json(force=True)
    return msg_controller.new_message(data)

@messages_bp.route("/messages/sent", methods=["GET"])
def get_all_sent():
    return message_controller.fetch_all_sent_messages("sent")
