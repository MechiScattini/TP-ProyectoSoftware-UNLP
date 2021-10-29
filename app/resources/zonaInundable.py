from flask import redirect, render_template, request, url_for, session

from app.models.ordenacion import Ordenacion
from app.helpers.auth import assert_permission
from app.models.elementos import Elementos
from app.models.zona_inundable import ZonaInundable

def index():
    """Controlador para listar las zonas inundables"""
    #Chequea autenticación y permisos
    assert_permission(session,'zona_inundable_index')

    #variables para paginación
    cant_paginas = Elementos.get_elementos()
    page = request.args.get('page', 1, type=int)

    #variable para opción de ordenación
    ordenacion = Ordenacion.get_ordenacion_zonas()

    #variable para opción de filtrado por estado: publicado o despublicado
    filter_option = request.args.get("filter_option")

    q = request.args.get("q") #query de búsqueda por nombre
    if q:
        zonas = ZonaInundable.get_zonas_busqueda(q, ordenacion.orderBy, page, cant_paginas)
    elif filter_option:
        zonas = ZonaInundable.get_zonas_con_filtro(filter_option, ordenacion.orderBy, page, cant_paginas)
    else:
        zonas = ZonaInundable.get_zonas_ordenados_paginados(ordenacion.orderBy, page, cant_paginas)
    return render_template("zona_inundable/index.html", zonas=zonas)

def show(id_zona):
    return render_template("zona_inundable/show.html")

def importar():
    pass

def destroy(id_zona):
    """Controlador para eliminar una zona inundable"""

    #Chequea autenticación y permisos
    assert_permission(session, 'zona_inundable_destroy')

    #busca y elimina
    ZonaInundable.delete_zona(id_zona)

    return redirect(url_for("zonaInundable_index"))