
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship, validates

from app.db import db
from app.models.status import Status

class PuntoEncuentro(db.Model):
    """Define una entidad de tipo Punto de Encuentro"""

    __tablename__ = "PuntosDeEncuentro"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), unique=True)
    direccion = Column(Text, nullable=False)
    coordenadas = Column(String(3)) 
    estado_id = Column(Integer, ForeignKey("statuses.id"))
    estado = relationship(Status)
    telefono = Column(String(30))
    email = Column(String(40))

    def __init__(self, nombre=None, direccion=None, coordenadas=None, estado_id=None, telefono=None, email=None):
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
        self.estado_id = estado_id
        self.telefono = telefono
        self.email = email
    
    @validates('direccion')
    def validate_direccion(self, key, direccion):
        if not direccion:
            raise ValueError("Debe ingresar una direccion")
        return direccion

    @validates('nombre')
    def validate_nombre(self, key, nombre):
        if not nombre:
            raise ValueError("Debe ingresar un nombre")
        return nombre

    @validates('email')
    def validate_email(self, key, email):
        if email and '@' not in email:
            raise ValueError("Ingrese un mail válido")
        return email