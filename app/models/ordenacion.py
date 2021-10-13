from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from sqlalchemy import update

from app.db import db


class Ordenacion(db.Model):
    """Define una entidad de tipo Ordenacion que se corresponde con el table ordenacion"""


    __tablename__ = "Ordenacion"
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer)

    def __init__(self, id_orden=None):
        self.id_orden = id_orden