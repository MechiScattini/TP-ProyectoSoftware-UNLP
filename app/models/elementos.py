from sqlalchemy import Column, Integer

from app.db import db


class Elementos(db.Model):
    """Define una entidad de tipo Elementos que se corresponde con el table elementos"""


    __tablename__ = "Elementos"
    id = Column(Integer, primary_key=True)
    cant = Column(Integer)

    def __init__(self, cant=None):
        self.cant = cant