from sqlalchemy import Column, Integer, String
from app import db

class UserInfo(db.Model):
    __tablename__ = "flask_userinfo"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(40), nullable=False)

    def __str__(self):
        return self.username
