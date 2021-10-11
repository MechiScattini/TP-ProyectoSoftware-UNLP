from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from sqlalchemy import update

from app.db import db


class Elementos(db.Model):
    """Define una entidad de tipo Status que se corresponde con el table elementos"""


    __tablename__ = "Elementos"
    id = Column(Integer, primary_key=True)
    cant = Column(Integer)

    def __init__(self, cant=None):
        self.cant = cant