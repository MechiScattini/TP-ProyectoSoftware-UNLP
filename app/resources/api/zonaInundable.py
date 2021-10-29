from flask import jsonify, Blueprint,json
from flask import abort
from app.models.zona_inundable import ZonaInundable
from app.helpers.codificador import decodificar
from app.models.elementos import Elementos

zona_api = Blueprint("zonas", __name__, url_prefix="/zonas-inundables")

@zona_api.get("/")
@zona_api.route('<page>')
def get_zonas(page):
    lista_zonas = []
    zonas = ZonaInundable.get_zonas()
    for zona in zonas:
        lista_zonas.append(
            {
                'id':zona.id, 
                'nombre':zona.nombre, 
                'coordenadas':decodificar(zona.coordenadas),
                'color':zona.color
            }
        )
    cant_per_pagina = Elementos.get_elementos()
    inicio=(int(page)-1)*cant_per_pagina
    lista_paginada = lista_zonas[inicio:inicio+cant_per_pagina]
    return jsonify(total=len(lista_paginada), pagina=page, zonas=lista_paginada)

@zona_api.get("/")
@zona_api.route('<id_zona>')
def get_zona(id_zona):
    zona = ZonaInundable.get_zona(id_zona)
    if not zona:
        abort(404) 
    return jsonify('atributos',
            {
                'id':zona.id, 
                'nombre':zona.nombre, 
                'coordenadas':decodificar(zona.coordenadas),
                'color':zona.color
            }
    )