import logging

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.helpers.extensions import mongo
import app.controllers.conference as conference


def create_app():
    app = Flask(__name__)
    Swagger(app)
    CORS(app)
    app.config.from_envvar('FLASK_CONFIG_FILE')
    app.logger.setLevel(logging.DEBUG)
    jwt = JWTManager(app)
    mongo.init_app(app)
    app.register_blueprint(conference.app)
    return app


if __name__ == "__main__":
    create_app().run(port=5001)
