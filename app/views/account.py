from flask import Blueprint, session, render_template, abort
from app import db
from app.models import UserInfo
ap = Blueprint("ap", __name__)


@ap.route("/login/")
def login():
    session["name"] = "Lance"
    # db.session.add(UserInfo(username="lance", password="LANCEyuan88"))
    # db.session.commit()
    # db.session.remove()
    data = db.session.query(UserInfo.username, UserInfo.password).all()
    print(data)
    return render_template("login.html")

@ap.route("/index/")
def index():
    return render_template("index.html", data="<h1>index</h1>")

@ap.app_template_filter() # 通过BLuePrint增加自定义filter
def make_up(text):
    return text.upper()

@ap.route('/index/<regex("\w{4,5}"):user_name>')
def user(user_name):
    return render_template("index.html", user=user_name)

# 注册一个400错误处理.
@ap.errorhandler(400)
def error_hander(e):
    return e, 400

@ap.route("/errors/")
def errors():
    abort(400) # 直接中断请求返回错误.
