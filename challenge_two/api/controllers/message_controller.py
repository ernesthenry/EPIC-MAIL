from flask import request, jsonify, json
from api.utilities.helpers import token_required, get_current_identity
from api.utilities.validation import validate_message
from api.models.message import user_messages, Message, get_sent_messages, get_specific_message

class MessageController:

    def new_message(self, data):
        data = request.get_json(force=True)
        if not request.data:
            return (
                jsonify(
                    {
                        "error": "No data returned form the request",
                        "status": 400,
                    }
                ),
                400,
            )

        message_data = {
            "subject": data.get("subject"),
            "message": data.get("message"),
            "sender_status": "sent",
            "reciever_status": "unread"
        }

        subject = data.get("subject")
        message = data.get("message")
        duplicate_message = [
            msg for msg in user_messages if msg["subject"] == subject
            ]
        if duplicate_message:
            return jsonify({
        "status": 409, 
        "error": "User already exists"
        }), 409

        invalid_message = validate_message(**message_data)

        if invalid_message:
            return jsonify({
                "status": 400, 
                "error": not_valid_user
                }), 400

        # message_data["userid"] = get_current_identity()
        new_message = Message(**message_data)
        user_messages.append(new_message.__dict__)
        return jsonify(
            {
                "status": 201,
                "data": [
                    {
                        "Message": new_message.__dict__,
                        }]
                        }),201

    def fetch_all_sent_messages(self, sender_status):
        all_messages = get_sent_messages(sender_status)

        if all_messages:
            return jsonify({
                "status": 200,
                "data": [message for message in all_messages],
                "message": "These are your sent messages"
            }), 200)
            
        else:
            return jsonify(
                    {"status": 404, "error": "You have not sent any mail yet."
                }), 404
            )

    def get_message(self, message_id):
        single_message = get_message(int(message_id))
        if single_message:
            return jsonify(
                {"status": 200,
                 "data": single_message
                 }), 200
        else:
            return jsonify(
                    {
                        "status": 404, 
                        "error": "Message  does not exist"
                    }),404
        