from .db import db,migrate
from flask import Flask 
from .config import Config
from .models import *
from .routes import message_bp

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(message_bp,url_prefix="/messages")

    return app