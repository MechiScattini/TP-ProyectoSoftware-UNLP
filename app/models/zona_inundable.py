from sqlalchemy import Column, String, SmallInteger, Boolean, Integer
from app.db import db

class ZonaInundabel(db.Model):
    """Define una entidad de zona inundable"""

    __tablename__ = "Zonas_inundables"
    id = Column(SmallInteger, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    #coordenadas = 
    estado = Column(Boolean,)
    color = Column(String(15))