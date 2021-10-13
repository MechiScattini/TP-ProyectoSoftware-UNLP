from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db
from sqlalchemy.orm import relationship

class Paletas(db.Model):
    """Define una entidad de tipo Paletas que se corresponde con el table paletas"""


    __tablename__ = "paletas"
    id = Column(Integer, primary_key=True)
    color_id = Column(Integer, ForeignKey("color.id"))

    def __init__(self, color_id=None):
        self.color_id = color_id