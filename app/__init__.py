from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # 且必须在蓝图之前导入.
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        super(RegexConverter, self).__init__(map)
        self.regex = args[0]

from .views.account import ap
from app.models import UserInfo

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object("settings.Dev")
    app.url_map.converters["regex"] = RegexConverter # 增加regex路由匹配.
    app.register_blueprint(ap)
    db.init_app(app)

    @app.template_filter("md") # flask filter
    def md(text): # 至少有一个参数，前端调用方式：data|md
        return "template_filter" + text
    return app
