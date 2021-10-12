from flask import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
from config import DevelopmentConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper


DB_USER= DevelopmentConfig.DB_USER
DB_NAME= DevelopmentConfig.DB_NAME
DB_PASS= DevelopmentConfig.DB_PASS
DB_USER= DevelopmentConfig.DB_USER
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost:3306/{DB_NAME}", echo = True)
Base = declarative_base()



""" se corresponde con el table users_roles"""
users_roles= Table ('users_roles', Base.metadata,
    Column('id' ,db.Integer, primary_key=True),
    Column('user_id' ,db.Integer, ForeignKey('users.id')),
    Column('rol_id', db.Integer, ForeignKey('roles.id')) )

"""class Users_roles(object):
    pass
mapper(Users_roles, users_roles)"""

""" se corresponde con el table roles_permisos"""
roles_permisos= Table ('roles_permisos', Base.metadata,
    Column('id' ,db.Integer, primary_key=True),
    Column('rol_id' ,db.Integer, ForeignKey('roles.id')),
    Column('permiso_id', db.Integer, ForeignKey('permisos.id')) )

"""class Roles_permisos(object):
    pass
mapper(Roles_permisos, roles_permisos)"""

class User(Base):
    """Define una entidad de tipo User que se corresponde con el table users"""

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
    

    def has_permission(user_id, permission):
        #permiso = db.session.query(Permiso).filter(Permiso.name == permission).first()
       # roles_con_permiso= db.session.query(Roles_permisos).filter(Roles_permisos.permiso_id == permiso.id)
        #for rol_con_permiso in roles_con_permiso:
          #  users_con_rol= db.session.query(Users_roles).filter(Users_roles.rol_id ==rol_con_permiso.rol_id)
            #for u in users_con_rol:
              #  if user_id == u:
                    return True
       # return False

class Permiso(Base):
    """Define una entidad de tipo Permiso que se corresponde con el table permisos"""

    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    roles = relationship( "Rol", secondary=roles_permisos, back_populates="permisos")
class Rol(Base):
    """Define una entidad de tipo Rol que se corresponde con el table roles"""

    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    users = relationship( "User", secondary=users_roles, back_populates="roles")
    permisos = relationship( "Permiso", secondary=roles_permisos, back_populates="roles")



Base.metadata.create_all(engine)