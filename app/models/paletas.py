from sqlalchemy import Column, Integer, String
from app.db import db

class Status(db.Model):
    """Define una entidad de tipo Status que se corresponde con el table statuses"""


    __tablename__ = "paletas"
    id = Column(Integer, primary_key=True)
    color_id = Column(Integer, ForeignKey("color.id"))
    color = relationship(Color)

    def __init__(self, color_id=None):
        self.color_id = color_id