from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy import exc

from app.models.puntoEncuentro import PuntoEncuentro
from app.helpers.auth import authenticated, check_permission
from app.db import db
from app.models.user import User

def index():
    if not authenticated(session):
        abort(401)

    user = User.query.filter(User.email==session['user'])

    if not check_permission(user[0].id, 'punto_encuentro_index'):
        abort(401) 
    
    #falta módulo de configuración para traer la cant de elementos por pagina
    #cantPaginas = Config.query....
    cantPaginas = 4 #puse 2 de prueba

    page = request.args.get('page', 1, type=int)
    puntos = PuntoEncuentro.query.paginate(page=page, per_page=cantPaginas)

    return render_template("puntoEncuentro/index.html", puntos=puntos)

def new():
    if not authenticated(session):
        abort(401)

    user = User.query.filter(User.email==session['user'])

    if not check_permission(user[0].id, 'punto_encuentro_new'):
        abort(401)
    
    return render_template("puntoEncuentro/new.html")

def create():
    if not authenticated(session):
        abort(401)

    user = User.query.filter(User.email==session['user'])

    if not check_permission(user[0].id, 'punto_encuentro_create'):
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
    if not authenticated(session):
        abort(401)

    user = User.query.filter(User.email==session['user'])

    if not check_permission(user[0].id, 'punto_encuentro_update'):
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
    if not authenticated(session):
        abort(401)

    user = User.query.filter(User.email==session['user'])

    if not check_permission(user[0].id, 'punto_encuentro_destroy'):
        abort(401)  
    
    punto = PuntoEncuentro.query.get_or_404(id_punto)
    db.session.delete(punto)
    db.session.commit()
    
    return redirect(url_for("puntoEncuentro_index"))

