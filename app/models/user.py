from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.selectable import subquery
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy import Column, Integer, ForeignKey

from app.db import db

""" se corresponde con el table users_roles"""
users_roles= db.Table ('users_roles',
    Column('id_users_roles', db.Integer, primary_key=True),
    Column('user_id' ,db.Integer, ForeignKey('users.id')),
    Column('rol_id', db.Integer, ForeignKey('roles.id')) 
    )

""" se corresponde con el table roles_permisos"""
roles_permisos= db.Table ('roles_permisos',
    Column('id_roles_permisos', db.Integer, primary_key=True),
    Column('rol_id' , db.Integer, ForeignKey('roles.id')),
    Column('permiso_id', db.Integer, ForeignKey('permisos.id')) )

class User(db.Model):
    """Define una entidad de tipo User que se corresponde con el table users"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30), unique=True)
    password = Column(String(300))
    bloqueado = Column(Boolean, default= False)
    username = Column(String(39),unique = True)
    roles = relationship( "Rol", secondary='users_roles', lazy='subquery', backref=db.backref('users',lazy='subquery'))
    
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
class Rol(db.Model):
    """Define una entidad de tipo Rol que se corresponde con el table roles"""

    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    
    permisos = relationship( "Permiso", secondary='roles_permisos',lazy='subquery', backref=db.backref('roles',lazy='subquery'))

class Permiso(db.Model):
    """Define una entidad de tipo Permiso que se corresponde con el table permisos"""

    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)