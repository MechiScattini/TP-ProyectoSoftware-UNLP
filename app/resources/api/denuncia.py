from flask import jsonify, Blueprint, request
from app.models.denuncia import Denuncia
from app.operations.operaciones_api import validate_denuncia

denuncia_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@denuncia_api.post("/")
def create():
    data = request.get_json()
    error = ""
    if 'categoria_id' not in data:
        error ="Debe enviar un campo categoria_id"
    if 'coordenadas' not in data:
        error ="Debe enviar un campo coordenadas"
    if 'apellido_denunciante' not in data:
        error ="Debe enviar un campo apellido_denunciante"
    if 'nombre_denunciante' not in data:
        error ="Debe enviar un campo nombre_denunciante"
    if 'telcel_denunciante' not in data:
        error ="Debe enviar un campo telcel_denunciante"
    if 'email_denunciante' not in data:
        error ="Debe enviar un campo email_denunciante"
    if 'titulo' not in data:
        error ="Debe enviar un campo titulo"
    if 'descripcion' not in data:
        error ="Debe enviar un campo descripcion"
    if error:
        return jsonify(error)
    response = validate_denuncia(**data)
    if response:
        return jsonify(response), 400
    denuncia = Denuncia.create_denuncia(**data)
    return jsonify(
        'atributos',
            {
                'categoria_id':denuncia.categoria_id,
                'apellido_denunciante':denuncia.apellido_denunciante, 
                'nombre_denunciante':denuncia.nombre_denunciante,
                'telcel_denunciante':denuncia.telefono_denunciante,
                'email_denunciante':denuncia.email_denunciante,
                'titulo':denuncia.titulo,
                'descripcion':denuncia.descripcion
            }
    ), 201