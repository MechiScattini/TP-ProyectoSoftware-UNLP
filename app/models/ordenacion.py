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

    def ordenUsuarios(ordenUsers):
        ordenU = Ordenacion.query.filter_by(lista = 'usuarios').first()
        if ordenU is not None: 
            ordenU.orderBy = ordenUsers
        else:
            ordenU = Ordenacion('nombre','usuarios')
            db.session.add(ordenU)
        db.session.commit()
        return ordenU  

    def ordenPuntos(ordenPuntos):
        ordenP = Ordenacion.query.filter_by(lista = 'puntos').first()
        if ordenP is not None: 
            ordenP.orderBy = ordenPuntos
        else:
            ordenP = Ordenacion('nombre','puntos')
            db.session.add(ordenP)
        db.session.commit()    
        return ordenP    