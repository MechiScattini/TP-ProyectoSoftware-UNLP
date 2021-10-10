from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30), unique=True)
    password = Column(String(30))
    bloqueado = Column(Boolean, default= False)
    username = Column(String,unique = True)
    
    def __init__(self, username=None,first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bloqueado = False
        self.username = username

class Permiso(db.Model):
    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

class Rol(db.Model):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)