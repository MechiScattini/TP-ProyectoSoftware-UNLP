from sqlalchemy import Column, Integer, String
from app.db import db

class Status(db.Model):
    """Define una entidad de tipo Status que se corresponde con el table statuses"""


    __tablename__ = "colores"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)

    def __init__(self, color_id=None):
        self.nombre = nombre