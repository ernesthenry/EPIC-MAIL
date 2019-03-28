import psycopg2
import psycopg2.extras
from pprint import pprint
from datetime import datetime
from werkzeug.security import generate_password_hash
from datetime import datetime


class DatabaseConnection:
    def __init__(self):

        self.db_name = 'epicmaildb'

        try:
            self.connection = psycopg2.connect(dbname=self.db_name, user="postgres",
                                               host="localhost", password="andela2018", port=5432)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            self.create_tables()

        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    def create_tables(self):
        create_tables = (
            """ CREATE TABLE IF NOT EXISTS users (
            id SERIAL NOT NULL PRIMARY KEY,
            email TEXT NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            password TEXT NOT NULL);
            """,

            """

            CREATE TABLE IF NOT EXISTS  messages (
                message_id SERIAL NOT NULL PRIMARY KEY,
                subject VARCHAR(125) NOT NULL,
                message TEXT NOT NULL,
                sender_status VARCHAR(50) NOT NULL,
                receiver_status VARCHAR(50) NOT NULL,
                parent_message_id INT NOT NULL,
                created_on  DATE DEFAULT CURRENT_TIMESTAMP,
                sender_id VARCHAR(50) NOT NULL,
                receiver_id INT NOT NULL);

            """,
            """
            CREATE TABLE IF NOT EXISTS groups(
                group_id SERIAL NOT NULL PRIMARY KEY,
                group_name VARCHAR(25) NOT NULL,
                role BOOLEAN DEFAULT FALSE);

            """,)
        for table in create_tables:
            self.cursor.execute(table)

    def register_user(self, email, firstname, lastname, password):
        """
        Register a user
        """

        reg_user = "INSERT INTO users(email, firstname, lastname, password) VALUES('{}','{}','{}','{}')".format(
            email, firstname, lastname, password)
        self.cursor.execute(reg_user)

    def check_email(self, email):
        """
        Check if an email already exists
        """
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def login(self, email):
        """
        Get login credentials for comarison to login
        """
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        pprint(user)
        return user

    def create_group(self, group_name, role):
        """Method for creating new group"""

        query = "INSERT INTO groups(group_name, role) VALUES('{}', '{}')".format(
            group_name, role)
        self.cursor.execute(query)
        return "Group created succesfully"

    def get_specific_group(self, group_id):
        """Method for getting  a specific group"""
        query = "SELECT * FROM groups WHERE group_id='{}' ".format(group_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all_groups(self):
        query = "SELECT * FROM groups;"
        self.cursor.execute(query)
        groups = self.cursor.fetchall()
        return groups

    def update_group_name(self,group_id, group_name):
        self.cursor.execute(
            "UPDATE groups SET group_name = %s WHERE group_id = %s",[group_id, group_name]
        )
        return "success"



    def check_duplicate_group(self, group_name):
        """
            Check if group already exists
        """
        query = "SELECT * FROM groups WHERE group_name='{}'".format(group_name)
        pprint(query)
        self.cursor.execute(query)
        group_name = self.cursor.fetchone()
        return group_name

    def create_message(self, **kwargs):
        """Method for creating a new message"""
        subject = kwargs.get("subject")
        message = kwargs.get("message")
        sender_status = "sent"
        receiver_status = "unread"
        receiver_id = kwargs.get("receiver_id")
        sender_id = kwargs.get("user_id")
        parent_message_id = kwargs.get("parent_message_id")
        created_on = datetime.now()

        query = "INSERT INTO messages(subject, message, sender_status, receiver_status, receiver_id, sender_id, parent_message_id, created_on) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(subject, message, sender_status, receiver_status, receiver_id, sender_id, parent_message_id, created_on)
        self.cursor.execute(query)
        message = self.cursor.fetchone()
        return message

    def check_duplicate_message(self, subject, message):
        """Testing for uniqueness of a message."""
        query = "SELECT subject, Message from messages where subject ='{}' and message='{}'".format(subject, message)
        self.cursor.execute(query)
        message_exists = self.cursor.fetchone()
        error = {}
        error_subject = "Subject arleady exists"
        error_message = "Message arleady exists"
        if message_exists and message_exists.get("subject") == subject:
            error["subject"] = error_subject

        if message_exists and message_exists.get("message") == message:
            error["message"] = error_message
        return error

    def get_specific_message(self, msg_id, owner_id):
        """Method for getting  a specific message"""
        query = "SELECT * FROM messages WHERE message_id='{}' AND receiver_id='{}'".format(msg_id, owner_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def delete_inbox_message(self, owner_id, msg_id):
        """Method to delete a given message from user inbox."""
        query = "SELECT * FROM messages WHERE receiver_id='{}' AND message_id='{}';".format(owner_id, msg_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_sent_messages(self, owner_id):
        """Function which returns all sent messages by a user."""
        query = "SELECT * FROM messages WHERE sender_id='{}';".format(owner_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all_received_unread_messages(self, owner_id):
        """Function for getting all received messages."""
        query = "SELECT * FROM messages WHERE receiver_status='{}';".format(owner_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def delete_inbox_mail(self, msg_id, user_id):
        """Function to delete a user's inbox mail."""
        query = "DELETE FROM messages WHERE receiver_id='{}' AND message_id='{}'".format(user_id, msg_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def drop_table(self, table_name):
        drop = "DROP TABLE '{}';".format(table_name)
        self.cursor.execute(drop)


if __name__ == '__main__':
    db_name = DatabaseConnection()
