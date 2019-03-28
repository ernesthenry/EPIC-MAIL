"""Application entry point"""
from api.views.home_route import app
from api.db import DatabaseConnection

my_db = DatabaseConnection()

if __name__ == "__main__":
    app.run(debug=True)