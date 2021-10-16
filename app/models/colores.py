from sqlalchemy import Column, Integer, String
from app.db import db

class Colores(db.Model):
    """Define una entidad de tipo colores que se corresponde con el table colores"""


    tablename = "colores"
    id = Column(Integer, primary_key=True)
    publico = Column(String(30))
    privado = Column(String(30))

    def init(self, publica=None, privada=None ):
        self.publico = publica
        self.privado = privada