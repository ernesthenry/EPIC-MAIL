from flask import Flask, Blueprint
from api.views.user_routes import user_blueprint
from api.views.message_routes import message_bp
from api.views.group_routes import group_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix="/api/v1")
    app.register_blueprint(message_bp, url_prefix="/api/v1" )
    app.register_blueprint(group_blueprint, url_prefix="/api/v1" )

    return app