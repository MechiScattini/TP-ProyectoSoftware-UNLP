from flask import redirect, render_template, request, url_for, session
from sqlalchemy import exc
from flask.helpers import flash

from app.models.ordenacion import Ordenacion
from app.models.denuncia import Denuncia
from app.helpers.auth import assert_permission
from app.db import db
from app.models.elementos import Elementos


def index():
    """ Muestra las denuncias del sistema """
    assert_permission(session,'denuncia_index')

    #paginacion
    page  = int(request.args.get('page', 1,type=int))

    cant_paginas = Elementos.get_elementos()

    #variable para opción de ordenación
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    if request.method == "GET":
        q = request.args.get("q")
        if q:
            denuncias= Denuncia.denuncias_por_busqueda(q,ordenacion ,page,cant_paginas)
        else:
            denuncias = Denuncia.paginacion(ordenacion, page, cant_paginas)
        return render_template("denuncia/index.html", denuncias=denuncias)


def sinConfirmar():
    """ Muestra las denuncias sin confirmar """
    assert_permission(session,'denuncia_sinConfirmar') 

    #chequeo si habia un orden creado
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    cant_paginas = Elementos.query.first()

    page  = int(request.args.get('page', 1,type=int))
    q = request.args.get("q")
    if q:
        denuncias= Denuncia.users_por_busqueda(q,ordenacion ,page,cant_paginas)
    else:
        denuncias = Denuncia.get_denuncias_sinConfirmar(ordenacion, page, cant_paginas)
    return render_template("denuncia/index.html", denuncias=denuncias)


def enCurso():
    """ Muestra las denuncias en curso """
    assert_permission(session,'denuncia_index') 

    #chequeo si habia un orden creado
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    cant_paginas = Elementos.query.first()

    page  = int(request.args.get('page', 1,type=int))
    q = request.args.get("q")
    if q:
        denuncias= Denuncia.users_por_busqueda(q,ordenacion ,page,cant_paginas)
    else:
        denuncias = Denuncia.get_denuncias_enCurso(ordenacion, page, cant_paginas)
    return render_template("denuncia/index.html", denuncias=denuncias)

def resuelta():
    """ Muestra las denuncias resueltas """
    assert_permission(session,'denuncia_index') 

    #chequeo si habia un orden creado
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    cant_paginas = Elementos.query.first()

    page  = int(request.args.get('page', 1,type=int))
    q = request.args.get("q")
    if q:
        denuncias= Denuncia.users_por_busqueda(q,ordenacion ,page,cant_paginas)
    else:
        denuncias = Denuncia.get_denuncias_resuelta(ordenacion, page, cant_paginas)
    return render_template("denuncia/index.html", denuncias=denuncias)

def cerrada():
    """ Muestra las denuncias cerradas """
    assert_permission(session,'denuncia_index') 

    #chequeo si habia un orden creado
    ordenacion = Ordenacion.get_ordenacion_denuncias()

    cant_paginas = Elementos.query.first()

    page  = int(request.args.get('page', 1,type=int))
    q = request.args.get("q")
    if q:
        denuncias= Denuncia.users_por_busqueda(q,ordenacion ,page,cant_paginas)
    else:
        denuncias = Denuncia.get_denuncias_cerrada(ordenacion, page, cant_paginas)
    return render_template("denuncia/index.html", denuncias=denuncias)




def new():
    """Controlador para mostrar el formulario para crear denuncias"""
    #Chequea autenticación y permisos
    assert_permission(session, 'denuncia_new')

    return render_template("denuncia/new.html")


def create():
    """Controlador para crear una denuncia"""

    #Chequea autenticación y permisos
    assert_permission(session, 'denuncia_create')

    #catchea todos los errores que levantan los validadores de campos
    if request.method == "POST":
        params = request.form   
        error = None
        if not params["titulo"]:
            error = 'Titulo es requerido'
        if not params["descripcion"]:
            error = 'Descripcion es requerido'
        elif not params["coordenadas"]:
            error = 'Coordenadas es requerido' 
        elif not params["apellido_denunciante"]:
            error = 'Apellido del denunciante es requerido'
        elif not params["nombre_denunciante"]:
            error = 'Nombre del denunciante es requerido'
        elif not params["telefono_denunciante"]:
            error = 'Telefono del denunciante es requerido'
        elif '@' not in params["email_denunciante"]:
            error = 'Ingrese un email valido'
            

def update():
    pass

def destroy(id_denuncia):
    """Controlador para eliminar una denuncia"""
    #Chequea autenticación y permisos
    assert_permission(session, 'denuncia_destroy')
    #busca y elimina
    denuncia = Denuncia.get_denuncia(id_denuncia)
    db.session.delete(denuncia)
    db.session.commit()
    return redirect(url_for("denuncia_index"))


def confirmar(denuncia_id):
    """Controlador para confirmar una denuncia"""
    #Chequea autenticación y permisos
    assert_permission(session, 'denuncia_confirmar')
    #busca y confirma
    denuncia = Denuncia.get_denuncia(denuncia_id)
    denuncia.estado_id=4
    denuncia.asignado_a=session["user2"].id
    db.session.commit()
    return redirect(url_for("denuncia_index"))

def cerrar(denuncia_id):
    """Controlador para cerrar una denuncia"""
    #Chequea autenticación y permisos
    assert_permission(session, 'denuncia_cerrar')
    #busca y confirma
    denuncia = Denuncia.get_denuncia(denuncia_id)
    if denuncia.estado_id != 3 :
        if denuncia.asignado_a == session["user2"].id :
            denuncia.estado_id=6
            db.session.commit()
    else:
        denuncia.estado_id=6
        db.session.commit()
    return redirect(url_for("denuncia_index"))

def resolver(denuncia_id):
    """Controlador para resolver una denuncia"""
    #Chequea que el user sea el que esta a cargo
    denuncia = Denuncia.get_denuncia(denuncia_id)
    if denuncia.asignado_a == session["user2"].id :
        denuncia.estado_id=5
        db.session.commit()
    return redirect(url_for("denuncia_index"))