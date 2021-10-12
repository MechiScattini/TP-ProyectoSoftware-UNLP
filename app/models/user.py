from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
from config import DevelopmentConfig
from sqlalchemy import create_engine

DB_USER= DevelopmentConfig.DB_USER
DB_NAME= DevelopmentConfig.DB_NAME
DB_PASS= DevelopmentConfig.DB_PASS
DB_USER= DevelopmentConfig.DB_USER
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost:3306/{DB_NAME}", echo = True)
Base = declarative_base()

users_roles= Table ('users_roles', Base.metadata,
    Column('id' ,db.Integer, primary_key=True),
    Column('user_id' ,db.Integer, ForeignKey('users.id')),
    Column('rol_id', db.Integer, ForeignKey('roles.id')) )

"""roles_permisos= Table ('roles_permisos', Base.metadata,
    Column('id' ,db.Integer, primary_key=True),
    Column('rol_id' ,db.Integer, ForeignKey('roles.id')),
    Column('permiso_id', db.Integer, ForeignKey('permisos.id')) )"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30), unique=True)
    password = Column(String(300))
    bloqueado = Column(Boolean, default= False)
    username = Column(String(39),unique = True)
    roles = relationship( "Rol", secondary=users_roles, back_populates="users")
    
    def __init__(self, username=None,first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bloqueado = False
        self.username = username
    

"""class Permiso(Base):
    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    roles = relationship( "Rol", secondary=users_roles, back_populates="permisos")"""
class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    users = relationship( "User", secondary=users_roles, back_populates="roles")
  #  permisos = relationship( "Permiso", secondary=roles_permisos, back_populates="roles")



Base.metadata.create_all(engine)