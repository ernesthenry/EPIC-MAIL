import psycopg2
import psycopg2.extras
from pprint import pprint
import os
from datetime import datetime


class DatabaseConnection:

    def __init__(self):

        if os.getenv('DB_NAME') == 'test_db':
            self.db_name = 'test_db'
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', port=5432
            )
        elif os.getenv('DB_NAME') == 'epicmaildb':
            self.db_name = 'epicmaildb'
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', password='andela2018', port=5432
            )
        try:

            self.connection.autocommit = True
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            print(self.db_name)

            create_user_table = "CREATE TABLE IF NOT EXISTS users (\
                                id SERIAL NOT NULL PRIMARY KEY,\
                                email TEXT NOT NULL,\
                                firstname TEXT NOT NULL,\
                                lastname TEXT NOT NULL,\
                                password TEXT NOT NULL);"

            self.cursor.execute(create_user_table)
        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    def register_user(self, email, firstname, lastname, password):
        """
        Register a user
        """
        reg_user = f"INSERT INTO users(email,firstname, lastname, password, email) VALUES('{email}','{firstname}','{lastname}','{password}');"
        pprint(reg_user)
        self.cursor.execute(reg_user)
        return reg_user


    def check_email(self, email):
        """
        Check if an email already exists
        """
        query = f"SELECT * FROM users WHERE email='{email}';"
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    
if __name__ == '__main__':
    db_name = DatabaseConnection()
