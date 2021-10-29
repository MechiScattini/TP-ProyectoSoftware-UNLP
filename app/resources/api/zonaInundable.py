from flask import jsonify, Blueprint,json
from app.models.zona_inundable import ZonaInundable
from app.helpers.codificador import decodificar

zona_api = Blueprint("zonas", __name__, url_prefix="/zonas-inundables")

@zona_api.get("/")
def get_zonas():
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

    return jsonify('zonas',lista_zonas)
    #return json.dumps(lista_zonas)

@zona_api.get("/")
@zona_api.route('<id_zona>')
def get_zona(id_zona):
    zona = ZonaInundable.get_zona(id_zona)
    return jsonify('atributos',
            {
                'id':zona.id, 
                'nombre':zona.nombre, 
                'coordenadas':decodificar(zona.coordenadas),
                'color':zona.color
            }
    )