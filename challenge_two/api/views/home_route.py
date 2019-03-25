
#api/controllers
from flask import Blueprint
from api import create_app
from api.controllers.home_controller import Home

app = create_app()

home_page = Home()
@app.route("/")
def first_page():
    return home_page.home()