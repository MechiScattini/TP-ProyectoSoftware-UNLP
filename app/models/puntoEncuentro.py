
from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.orm import validates
from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.colores import Colores
from app.db import db

class PuntoEncuentro(db.Model):
    """Define una entidad de tipo Punto de Encuentro"""

    __tablename__ = "puntos_de_encuentro"
    id = Column(SmallInteger, primary_key=True)
    nombre = Column(String(40), unique=True, nullable=False)
    direccion = Column(String(30), unique=True, nullable=False)
    coordenadas = Column(String(80)) 
    estado = Column(Boolean)
    telefono = Column(String(30))
    email = Column(String(40))

    def __init__(self, nombre=None, direccion=None, coordenadas=None, estado=None, telefono=None, email=None):
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
        self.estado_id = estado
        self.telefono = telefono
        self.email = email
    
    def per_page():
        elem = Elementos.query.first()
        if elem is not None:
            per_page = int(elem.cant)
        else:
            per_page = 4
        return per_page

    def paginacion():
        #variable para opción de ordenación
        ordenacion = Ordenacion.query.filter_by(lista='puntos').first()
        if not ordenacion:
            #si no hay nada en la db pone por defecto ordenar por nombre
            ordenacion = Ordenacion('nombre','puntos')
        return ordenacion
    def colores ():
        #aca agarro el color 
        colores = Colores.query.filter_by(id=1).first()
        if colores is None:
            color = "rojo"
        else:
            color = colores.privado
        return color

    @validates('direccion')
    def validate_direccion(self, key, direccion):
        """Valida el campo dirección"""

        if not direccion:
            raise ValueError("Debe ingresar una direccion")
        return direccion

    @validates('nombre')
    def validate_nombre(self, key, nombre):
        """Valida el campo nombre"""

        if not nombre:
            raise ValueError("Debe ingresar un nombre")
        return nombre

    @validates('email')
    def validate_email(self, key, email):
        """Valida el campo email"""

        if email and '@' not in email:
            raise ValueError("Ingrese un mail válido")
        return email
