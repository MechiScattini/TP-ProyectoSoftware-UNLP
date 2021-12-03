from flask import jsonify, Blueprint,request
from app.models.puntoEncuentro import PuntoEncuentro
from app.models.zona_inundable import ZonaInundable
from app.models.denuncia import Denuncia
from app.models.recorrido import Recorrido
from app.helpers.codificador import decodificar
from app.models.elementos import Elementos


estadisticas_api = Blueprint("estadisticas", __name__, url_prefix="/estadisticas")

@estadisticas_api.get("/")
def index():
    lista = []
    cant_puntos = PuntoEncuentro.get_cantidad()
    cant_recorridos = Recorrido.get_cantidad()
    cant_denuncias = Denuncia.get_cantidad()
    cant_zonasInundables = ZonaInundable.get_cantidad()

    lista.append(
        {
            'cantidad puntos ':cant_puntos, 
            'cantidad recorridos ':cant_recorridos, 
            'cantidad denuncias ':cant_denuncias,
            'cantidad zonas inundables ':cant_zonasInundables,
        }

    )
    return jsonify(lista)