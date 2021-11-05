from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql.selectable import subquery
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy import Column, Integer, ForeignKey
from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.colores import Colores

from app.db import db

""" se corresponde con el table users_roles"""
users_roles= db.Table ('users_roles',
    Column('id_users_roles', db.Integer, primary_key=True),
    Column('user_id' ,db.SmallInteger, ForeignKey('users.id')),
    Column('rol_id', db.SmallInteger, ForeignKey('roles.id')) 
    )

""" se corresponde con el table roles_permisos"""
roles_permisos= db.Table ('roles_permisos',
    Column('id_roles_permisos', db.Integer, primary_key=True),
    Column('rol_id' , db.SmallInteger, ForeignKey('roles.id')),
    Column('permiso_id', db.SmallInteger, ForeignKey('permisos.id')) )

class User(db.Model):
    """Define una entidad de tipo User que se corresponde con el table users"""

    __tablename__ = "users"
    id = Column(SmallInteger, primary_key=True)
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
        user = User.query.filter(User.id==user_id).first()
        permisos = []
        nombres_permisos = []
        for rol in user.roles:
            permisos.append(rol.permisos)
        for a in permisos:
            for permiso in a:
                nombres_permisos.append(permiso.name)

        return permission in nombres_permisos

    
    def per_page():
        elem = Elementos.query.first()
        if elem is not None:
            per_page = int(elem.cant)
        else:
            per_page = 2
        return per_page

    
    def paginacion(per_page,page):
        orden = Ordenacion.query.filter_by(lista='usuarios').first()
        #chequeo si habia un orden creado
        if orden is None:
            orden = Ordenacion("email","usuarios")
        return db.session.query(User).order_by(orden.orderBy).paginate(page,per_page,error_out=False)


    def allUsers():
        return db.session.query(User).all()

       
    def color ():
        #aca agarro el color 
        colores = Colores.query.filter_by(id=1).first()
        if colores is None:
            color = "rojo"
        else:
            color = colores.privado
        return color
                
class Rol(db.Model):
    """Define una entidad de tipo Rol que se corresponde con el table roles"""

    __tablename__ = 'roles'
    id = Column(SmallInteger, primary_key=True)
    name = Column(String(30), unique=True)
    permisos = relationship( "Permiso", secondary='roles_permisos',lazy='subquery', backref=db.backref('roles',lazy='subquery'))

class Permiso(db.Model):
    """Define una entidad de tipo Permiso que se corresponde con el table permisos"""

    __tablename__ = "permisos"
    id = Column(SmallInteger, primary_key=True)
    name = Column(String(30), unique=True)