from sqlalchemy import Column, Integer, String, SMALLINT
from app.db import db
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.expression import desc, select

class Status(db.Model):
    """Define una entidad de tipo Status que se corresponde con el table statuses"""

    __tablename__ = "statuses"
    id = Column(SMALLINT, primary_key=True)
    name = Column(String(30), unique=True)

    def __init__(self, name=None):
        self.name = name


    @classmethod
    def get_all(self):
        return Status.query.all()