from sqlalchemy import Column, String, SmallInteger, Boolean, Integer
from app.db import db

class ZonaInundable(db.Model):
    """Define una entidad de zona inundable"""

    __tablename__ = "Zonas_inundables"
    id = Column(SmallInteger, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(30), unique=True, nullable=False)
    coordenadas = Column(String(1000),nullable=False)
    estado = Column(Boolean)
    color = Column(String(15))

    def __init__(self, codigo=None, nombre=None, coordenadas=None, estado=None, color=None):
        self.codigo = codigo
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.estado = estado
        self.color = color

    @classmethod
    def get_zonas(self):
        return ZonaInundable.query.all()

    @classmethod
    def get_zona(self, id_zona):
        return ZonaInundable.query.get(id_zona)

    @classmethod
    def get_zonas_busqueda(self, q, criterio_orden, pagina, cant_pagina):
        return ZonaInundable\
        .query\
        .filter(ZonaInundable.nombre.contains(q))\
        .order_by(criterio_orden)\
        .paginate(page=pagina, per_page=cant_pagina)

    @classmethod
    def get_zonas_ordenados_paginados(
        self,
        criterio_orden,
        pagina,
        cant_pagina
        ):
        return ZonaInundable\
        .query\
        .order_by(criterio_orden)\
        .paginate(page=pagina, per_page=cant_pagina)

    @classmethod
    def get_zonas_con_filtro(
        self,
        filter_option,
        criterio_orden,
        pagina,
        cant_pagina
    ):
        if filter_option == '1':
            zonas = ZonaInundable\
            .query\
            .filter(ZonaInundable.estado == True)\
            .order_by(criterio_orden)\
            .paginate(page=pagina, per_page=cant_pagina)
        else:
            zonas = ZonaInundable\
            .query\
            .filter(ZonaInundable.estado == False)\
            .order_by(criterio_orden)\
            .paginate(page=pagina, per_page=cant_pagina)
        return zonas

    @classmethod
    def delete_zona(self, id_zona):
        zona = ZonaInundable.get_zona(id_zona)
        db.session.delete(zona)
        db.session.commit()