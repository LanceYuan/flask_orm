from flask import Blueprint, session, render_template
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