import psycopg2
import psycopg2.extras
from pprint import pprint
from datetime import datetime
from werkzeug.security import generate_password_hash


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
                is_admin BOOLEAN DEFAULT FALSE);

            """
        )

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
