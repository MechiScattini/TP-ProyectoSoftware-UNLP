from sqlalchemy import Column, Integer, String

from app.db import db


class Ordenacion(db.Model):
    """Define una entidad de tipo Ordenacion que se corresponde con el table ordenacion"""


    __tablename__ = "ordenacion"
    id = Column(Integer, primary_key=True)
    orderBy = Column(String(50))
    lista = Column(String(50))

    def __init__(self, orderBy=None, lista = None):
        self.orderBy = orderBy
        self.lista = lista

    @classmethod
    def get_ordenacion_puntos(self):
        orden =  Ordenacion.query.filter_by(lista='puntos').first()
        if not orden:
            orden = Ordenacion('nombre','puntos')
        return orden
