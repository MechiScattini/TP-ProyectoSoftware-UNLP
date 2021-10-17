from typing import OrderedDict
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
    ordenPuntos = Ordenacion.query.filter_by(lista = 'puntos').first()
    ordenUsuarios = Ordenacion.query.filter_by(lista = 'usuarios').first()
    colores = Colores.query.first()
    if colores is None:
        color = "rojo"
        colores = Colores('rojo','rojo')
    else:
        color = colores.privado
    if not elem:
        elem = Elementos(4)
    if not ordenPuntos:
        ordenPuntos = Ordenacion('nombre','puntos')
    if not ordenUsuarios:
        ordenUsuarios = Ordenacion('nombre','ususarios')
    return render_template("config.html", cant = elem.cant, ordenP = ordenPuntos.orderBy, ordenU = ordenUsuarios.orderBy, coloresPriv = colores.privado, coloresPub = colores.publico, color = color)


def configurado():
    #Acá actualizo en la bd los nuevos valores ingresados
    col = Colores.query.first()
    if col is not None: 
        col.privado = str(request.form.get('colorPri'))
        col.publico = str(request.form.get('colorPub'))
    else:
        col = Colores('rojo','rojo')
        db.session.add(col)
    db.session.commit()
    ordenU = Ordenacion.query.filter_by(lista = 'usuarios').first()
    if ordenU is not None: 
        ordenU.orderBy = str(request.form.get('orden_usuarios'))
    else:
        ordenU = Ordenacion('nombre','usuarios')
        db.session.add(ordenU)
    db.session.commit()

    ordenP = Ordenacion.query.filter_by(lista = 'puntos').first()
    if ordenP is not None: 
        ordenP.orderBy = str(request.form.get('orden_puntos'))
    else:
        ordenP = Ordenacion('nombre','puntos')
        db.session.add(ordenP)
    elem = Elementos.query.first()
    if elem is not None:
        if request.form.get('numero'):
            elem.cant = int(request.form.get('numero'))
    else:
        elem = Elementos(4)
    db.session.commit()
    return redirect(url_for("home"))     