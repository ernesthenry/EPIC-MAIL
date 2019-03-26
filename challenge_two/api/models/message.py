from datetime import datetime
import uuid
user_messages = []


class Message:
    """class to contain all message objects"""
    def __init__(self, **kwargs):
        self._id= len(user_messages)+1
        self.subject = kwargs["subject"]
        self.message = kwargs["message"]
        self.sender_status = kwargs["sender_status"]
        self.reciever_status = "unread"
        self.parent_message_id = int(uuid.uuid4())
        self.created_on = str(datetime.now())
