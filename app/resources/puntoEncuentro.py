from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy import exc
from app.models.ordenacion import Ordenacion

from app.models.puntoEncuentro import PuntoEncuentro
from app.helpers.auth import authenticated, check_permission
from app.db import db
from app.models.user import User
from app.models.elementos import Elementos

def index():
    #Chequea autenticación y permisos
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).filter(User.email==session['user']).first()
    if not check_permission(user.id, 'punto_encuentro_index'):
        abort(401) 
    
    #variables para paginación
    elem = Elementos.query.filter_by(id=1).first()
    cantPaginas = elem.cant 
    page = request.args.get('page', 1, type=int)

    #variable para opción de ordenación
    ordenacion = Ordenacion.query.filter_by(id=1).first()
    if ordenacion.id_orden == 1:
        opcion_orden = 'email'
    else:
        opcion_orden = 'nombre'
    #variable para opción de filtrado: por nombre o estado
    filter_option = request.args.get("filter_option") 

    q = request.args.get("q") #query de búsqueda por nombre
    if q:
        puntos = PuntoEncuentro.query.filter(PuntoEncuentro.nombre.contains(q)).order_by(opcion_orden).paginate(page=page, per_page=cantPaginas)
    elif filter_option:
        puntos = PuntoEncuentro.query.filter(PuntoEncuentro.estado_id.contains(filter_option)).order_by(opcion_orden).paginate(page=page, per_page=cantPaginas)
    else:
        puntos = PuntoEncuentro.query.order_by(opcion_orden).paginate(page=page, per_page=cantPaginas)

    return render_template("puntoEncuentro/index.html", puntos=puntos, user=user)

def new():
    #Chequea autenticación y permisos
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).filter(User.email==session['user']).first()
    if not check_permission(user.id, 'punto_encuentro_new'):
        abort(401)
    
    return render_template("puntoEncuentro/new.html")

def create():
    #Chequea autenticación y permisos
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).filter(User.email==session['user']).first()
    if not check_permission(user.id, 'punto_encuentro_create'):
        abort(401) 

    #catchea todos los errores que levantan los validadores de campos
    try:
        new_punto = PuntoEncuentro(**request.form)
    except ValueError as e:
        flash(e)
        return render_template("puntoEncuentro/new.html")
    else:
        db.session.add(new_punto)

    #si el nombre ingresado o direccion ya se encuentra registrado en la db se produce la exeption
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
    #Chequea autenticación y permisos
    if not authenticated(session):
        abort(401)
    user =db.session.query(User).filter(User.email==session['user']).first()
    if not check_permission(user.id, 'punto_encuentro_update'):
        abort(401) 

    punto = PuntoEncuentro.query.get_or_404(id_punto)
    if request.method == 'POST':
        punto.coordenadas = request.form['coordenadas']
        punto.estado_id = request.form['estado_id']
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
    #Chequea autenticación y permisos
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).filter(User.email==session['user']).first()
    if not check_permission(user.id, 'punto_encuentro_destroy'):
        abort(401)  
    
    #busca y elimina
    punto = PuntoEncuentro.query.get_or_404(id_punto)
    db.session.delete(punto)
    db.session.commit()
    return redirect(url_for("puntoEncuentro_index"))

