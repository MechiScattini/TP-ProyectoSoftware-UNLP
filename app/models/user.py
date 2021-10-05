from enum import unique
from sqlalchemy import Column, Integer, String
from app.db import db

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), unique=True)
    last_name = Column(String(30), unique=True)
    email = Column(String(30), unique=True)
    password = Column(String(30), unique=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
