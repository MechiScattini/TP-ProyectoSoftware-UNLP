from flask import redirect, render_template, request, url_for, session, abort, flash

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
    cantPaginas = 2 #puse 2 de prueba

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

    #chequea los datos ingresados 
    if len(request.form['coordenadas']) > 3:
        flash("Las coordenadas deben tener formato x,y")
        return render_template("puntoEncuentro/new.html")

    new_punto = PuntoEncuentro(**request.form)
    db.session.add(new_punto)
    db.session.commit()

    return redirect(url_for("puntoEncuentro_index"))
