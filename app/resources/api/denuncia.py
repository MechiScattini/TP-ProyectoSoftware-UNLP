from flask import jsonify, Blueprint, request
from app.models.category import Category
from app.models.denuncia import Denuncia
from app.models.status import Status
from app.operations.operaciones_api import validate_denuncia
from app.helpers.codificador import decodificar
from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion

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

@denuncia_api.get("/")
def get_denuncias_confirmadas():
    lista_denuncias = []
    cant_per_page = Elementos.get_elementos()
    page = request.args.get('page',1,type=int)
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    denuncias = Denuncia.get_denuncias_enCurso(ordenacion,page,cant_per_page)
    for denuncia in denuncias.items:
        categoria = Category.get_categoria_id(denuncia.categoria_id)
        estado = Status.get_status(denuncia.estado_id)
        lista_denuncias.append(
            {
                'id':denuncia.id, 
                'titulo':denuncia.titulo, 
                'descripcion': denuncia.descripcion,
                'coordenadas':decodificar(denuncia.coordenadas),
                'categoria': categoria.name,
                'estado': estado.name
            }
        )
    return jsonify(total=len(lista_denuncias), pagina=page, denuncias=lista_denuncias)