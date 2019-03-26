from datetime import datetime
import uuid
user_messages = []


class Message:
    """class to contain all message objects"""
    def __init__(self, **kwargs):
        self.message_id= len(user_messages)+1
        self.subject = kwargs["subject"]
        self.message = kwargs["message"]
        self.sender_status = kwargs["sender_status"]
        self.reciever_status = "unread"
        self.parent_message_id = int(uuid.uuid4())
        self.created_on = str(datetime.now())

    def get_sent_messages(sender_status):
    """ Method that returns all  messages  sent by a user. """
    sent_messages = [
        message for message in user_messages
        if message["sender_status"] == "sent" 
    ]
    return sent_messages

    def get_specific_message(message_id):
    """ Method that  returns a specific message """
    specific_messsage = [
        message for message in user_messages
        if message["message_id"] == message_id
    ]
    return specific_messsage
