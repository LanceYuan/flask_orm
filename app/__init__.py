from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # 且必须在蓝图之前导入.

from .views.account import ap
from app.models import UserInfo

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object("settings.Dev")

    app.register_blueprint(ap)
    db.init_app(app)

    return app