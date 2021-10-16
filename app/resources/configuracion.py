from flask import redirect, render_template, request, url_for, session

from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.colores import Colores
from app.models.issue import Issue
from app.db import db
from sqlalchemy import update
from sqlalchemy import select
# Public resources

def conf():
    #return a la vista
    elem = Elementos.query.first()
    return render_template("config.html", cant = elem.cant)


def configurado():
    #Acá actualizo en la bd los nuevos valores ingresados
    col = Colores.query.filter_by(id = 1).first()
    if col is not None: 
        col.publico = str(request.form.get('color'))
    db.session.commit()
    orden = Ordenacion.query.filter_by(lista = 'usuarios').first()
    if orden is not None: 
        orden.orderBy = str(request.form.get('orden_usuarios'))
    db.session.commit()
    # orden = Ordenacion.query.filter_by(lista = 'puntos').first()
    # if orden is not None: 
    #     orden.orderBy = str(request.form.get('orden_puntos'))
    # db.session.commit()
    elem = Elementos.query.filter_by(id = 1).first()
    if elem is not None:
        if request.form.get('numero'):
            elem.cant = int(request.form.get('numero'))
    db.session.commit()
    return redirect(url_for("home"))     