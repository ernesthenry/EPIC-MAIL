
from flask import Blueprint, request
from api.controllers.message_controller import MessageController
from api.utilities.helpers import token_required

msg_controller = MessageController()

message_bp = Blueprint("message_bp", __name__)

@message_bp.route("/messages", methods = ["POST"])
def message():
    data = request.get_json(force=True)
    return msg_controller.new_message(data)

@message_bp.route("/messages/sent", methods=["GET"])
def get_all_sent():
    return msg_controller.fetch_all_sent_messages("sent")

@message_bp.route("/messages/<message_id>", methods=["GET"])
def get_specific_message(message_id):
    return msg_controller.get_message(message_id)

@message_bp.route("/messages/<message_id>", methods=["DELETE"])
def delete_specific_message(message_id):
    return msg_controller.delete_email(message_id)

@message_bp.route("/messages/unread", methods=["GET"])
def received_mails():
    return msg_controller.received_unread_emails("received")
