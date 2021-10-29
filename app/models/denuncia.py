from datetime import datetime
from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.expression import desc, select
from sqlalchemy.sql.sqltypes import Date, DateTime, Integer
from sqlalchemy import Column, Integer, ForeignKey
from app.db import db
from app.models.category import Category
from app.models.status import Status


'''
""" se corresponde con el table denuncias_seguimientos"""
denuncias_seguimientos= db.Table ('denuncias_seguimientos',
    Column('id_denuncias_seguimientos', db.Integer, primary_key=True),
    Column('denuncia_id' , db.SmallInteger, ForeignKey('denuncia.id')),
    Column('seguimiento_id', db.SmallInteger, ForeignKey('seguimiento.id')) )
'''

class Denuncia(db.Model):
    """Define una entidad de tipo Denuncia"""

    __tablename__ = "denuncia"
    id = Column(SmallInteger, primary_key=True)
    titulo = Column(String(40), unique=True, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now())
    fecha_cierre = Column(DateTime)
    descripcion = Column(String(80), nullable=False)
    coordenadas = Column(String(200), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categories.id"))
    estado_id = Column(Integer, ForeignKey("statuses.id"))
    asignado_a = Column(String(30))   #Este campo no se si esta bien declarado
    apellido_denunciante = Column(String(20), nullable=False)
    nombre_denunciante = Column(String(20), nullable=False)
    telefono_denunciante = Column(Integer, nullable=False)
    email_denunciante = Column(String(30), nullable=False)
   #seguimientos = relationship("Seguimiento", secondary='denuncias_seguimientos',lazy='subquery', backref=db.backref('seguimientos',lazy='subquery'))


    def __init__(
        self, titulo=None,
        fecha_cierre=None,
        descripcion=None,
        coordenadas=None,
        categoria_id=None,
        asignado_a=None,
        apellido_denunciante=None,
        nombre_denunciante=None,
        telefono_denunciante=None,
        email_denunciante=None
        ):
        self.titulo = titulo
        self.fecha_cierre = fecha_cierre
        self.descripcion = descripcion
        self.coordenadas = coordenadas
        self.categoria_id = None
        self.asignado_a = asignado_a
        self.apellido_denunciante = apellido_denunciante
        self.nombre_denunciante = nombre_denunciante
        self.telefono_denunciante = telefono_denunciante
        self.email_denunciante = email_denunciante


    @classmethod
    def get_denuncia(self, denuncia_id):
        return Denuncia.query.get(denuncia_id)

    @classmethod
    def denuncias_por_busqueda(self, q, orden, pagina, cant_paginas):
        return Denuncia.query.filter(Denuncia.titulo.contains(q)).order_by(orden.orderBy).paginate(page=pagina,per_page=cant_paginas,error_out=False)  

    @classmethod
    def paginacion(self,orden,pagina,cant_paginas):
        return Denuncia.query.order_by(orden.orderBy).paginate(page=pagina, per_page=cant_paginas)

    @classmethod
    def get_denuncias_enCurso(self,orden,pagina,cant_paginas):
        return Denuncia.query.filter(Denuncia.estado == 'En curso').order_by(orden.orderBy).paginate(page=pagina, per_page=cant_paginas)

    @classmethod
    def get_denuncias_resuelta(self,orden,pagina,cant_paginas):
        return Denuncia.query.filter(Denuncia.estado == 'Resuelta').order_by(orden.orderBy).paginate(page=pagina, per_page=cant_paginas)
        
    @classmethod
    def get_denuncias_cerrada(self,orden,pagina,cant_paginas):
        return Denuncia.query.filter(Denuncia.estado == 'Cerrada').order_by(orden.orderBy).paginate(page=pagina, per_page=cant_paginas)



class Seguimiento(db.Model):
    """Define una entidad de tipo Seguimiento"""

    __tablename__ = 'seguimientos'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(String(80))
    autor = Column(String(20))
    fecha = Column(Date)

'''
class Category(db.Model):
    """Define una entidad de tipo Category que se corresponde con el table categories"""

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    denuncias = relationship('Denuncia', backref="category", lazy=select)

    def __init__(self, name=None):
        self.name = name

class Status(db.Model):
    """Define una entidad de tipo Status que se corresponde con el table statuses"""

    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    denuncias = relationship('Denuncia', backref="status", lazy=select)

    def __init__(self, name=None):
        self.name = name

'''