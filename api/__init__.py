from flask import Flask, Blueprint
from api.views.user_routes import user_blueprint
from api.views.message_routes import message_bp
from api.views.group_routes import group_blueprint
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)



def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix="/api/v2")
    app.register_blueprint(message_bp, url_prefix="/api/v2" )
    app.register_blueprint(group_blueprint, url_prefix="/api/v2" )

    app.config['JWT_SECRET_KEY'] = '567890-=edjcnvcdsd9puf3q4jwptjfcepqxmn bfvd/z.fdjn '
    JWTManager(app)

    return app