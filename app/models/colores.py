from sqlalchemy import Column, Integer, String
from app.db import db

class Colores(db.Model):
    """Define una entidad de tipo colores que se corresponde con el table colores"""


    tablename = "colores"
    id = Column(Integer, primary_key=True)
    publico = Column(String(30))
    privado = Column(String(30))

    def __init__(self, publica=None, privada=None ):
        self.publico = publica
        self.privado = privada
    
    @classmethod
    def get_color_privado(self):
        colores = Colores.query.first()
        if colores is None:
            color = "rojo"
        else:
            color = colores.privado
        return color
    
    @classmethod
    def get_color_publico(self):
        colores = Colores.query.first()
        if colores is None:
            color = "rojo"
        else:
            color = colores.publico
        return color