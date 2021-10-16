from flask import redirect, render_template, request, url_for, session, flash
from sqlalchemy import exc

from app.models.ordenacion import Ordenacion
from app.models.puntoEncuentro import PuntoEncuentro
from app.helpers.auth import assert_permission
from app.db import db
from app.models.elementos import Elementos

def index():
    """Controlador para mostrar el listado de puntos de encuentro"""

    #Chequea autenticación y permisos
    assert_permission(session, 'punto_encuentro_index')

    #variables para paginación
    elem = Elementos.query.first()
    if elem:
        cantPaginas = elem.cant 
    else: #si no hay nada cargado en la db asigna 4 por defecto
        cantPaginas = 4
    page = request.args.get('page', 1, type=int)

    #variable para opción de ordenación
    ordenacion = Ordenacion.query.filter_by(lista='puntos').first()
    if not ordenacion:
        #si no hay nada en la db pone por defecto ordenar por nombre
        ordenacion = Ordenacion('nombre','puntos')

    #variable para opción de filtrado por estado: publicado o despublicado
    filter_option = request.args.get("filter_option") 

    q = request.args.get("q") #query de búsqueda por nombre
    if q:
        puntos = PuntoEncuentro.query.filter(PuntoEncuentro.nombre.contains(q)).order_by(ordenacion.orderBy).paginate(page=page, per_page=cantPaginas)
    elif filter_option:
        if filter_option == '1':
            puntos = PuntoEncuentro.query.filter(PuntoEncuentro.estado == True).order_by(ordenacion.orderBy).paginate(page=page, per_page=cantPaginas)
        else:
            puntos = PuntoEncuentro.query.filter(PuntoEncuentro.estado == False).order_by(ordenacion.orderBy).paginate(page=page, per_page=cantPaginas)
    else:
        puntos = PuntoEncuentro.query.order_by(ordenacion.orderBy).paginate(page=page, per_page=cantPaginas)

    return render_template("puntoEncuentro/index.html", puntos=puntos)

def new():
    """Controlador para mostrar el formulario para crear puntos de encuentro"""
    #Chequea autenticación y permisos
    assert_permission(session, 'punto_encuentro_new')
    
    return render_template("puntoEncuentro/new.html")

def create():
    """Controlador para crear un punto de encuentro"""

    #Chequea autenticación y permisos
    assert_permission(session, 'punto_encuentro_create')

    #catchea todos los errores que levantan los validadores de campos
    try:
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        coordenadas = request.form['coordenadas']
        estado = int(request.form['estado'])
        telefono = request.form['telefono']
        email = request.form['email']
        new_punto = PuntoEncuentro(nombre, direccion, coordenadas, estado, telefono, email)
    except ValueError as e:
        flash(e)
        return render_template("puntoEncuentro/new.html")
    else:
        db.session.add(new_punto)

    #si el nombre ingresado o direccion ya se encuentra registrado en la db se produce maneja las excepciones
    try:
        db.session.commit()
    except exc.IntegrityError as e:
        if 'direccion' in e.orig.args[1]:
            flash("Ya existe un punto con esa direccion")
        elif 'nombre' in e.orig.args[1]:
            flash("Ya existe un punto con ese nombre")
        return render_template("puntoEncuentro/new.html")

    return redirect(url_for("puntoEncuentro_index"))

def update(id_punto):
    """Controlador para editar un punto de encuentro"""

    #Chequea autenticación y permisos
    assert_permission(session, 'punto_encuentro_update')

    punto = PuntoEncuentro.query.get_or_404(id_punto)
    if request.method == 'POST':
        punto.coordenadas = request.form['coordenadas']
        punto.estado = int(request.form['estado'])
        punto.telefono = request.form['telefono']
        try:
            punto.nombre = request.form['nombre']
            punto.direccion = request.form['direccion']
            punto.email = request.form['email']
            db.session.commit()
        except exc.IntegrityError as e: #maneja las excepciones de datos ya ingresados en db
            if 'direccion' in e.orig.args[1]:
                flash("Ya existe un punto con esa direccion")
            elif 'nombre' in e.orig.args[1]:
                flash("Ya existe un punto con ese nombre")
            db.session.rollback()
            return render_template("puntoEncuentro/edit.html", puntoEncuentro=punto) 
        except ValueError as e: #maneja la validación de los campos
            flash(e)
            db.session.rollback()
            return render_template("puntoEncuentro/edit.html", puntoEncuentro=punto)
        flash("Punto actualizado")
        return redirect(url_for("puntoEncuentro_index")) 
    return render_template('puntoEncuentro/edit.html', puntoEncuentro=punto)

def destroy(id_punto):
    """Controlador para eliminar un punto de encuentro"""

    #Chequea autenticación y permisos
    assert_permission(session, 'punto_encuentro_destroy')
    
    #busca y elimina
    punto = PuntoEncuentro.query.get_or_404(id_punto)
    db.session.delete(punto)
    db.session.commit()
    return redirect(url_for("puntoEncuentro_index"))

