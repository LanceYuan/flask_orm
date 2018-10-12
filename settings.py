import datetime


class Base():
    SECRET_KEY = "flask_session_key"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://lance:LANCEyuan88@127.0.0.1:3306/codepy?charset=utf8"

class Dev(Base):
    DEBUG = True