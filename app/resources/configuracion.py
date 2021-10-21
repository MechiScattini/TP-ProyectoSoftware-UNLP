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
    Colores.configurar(request.form.get('colorPri'),request.form.get('colorPub'))
    ordenU = Ordenacion.ordenUsuarios(request.form.get('orden_usuarios'))
    ordenP = Ordenacion.ordenPuntos(request.form.get('orden_puntos'))    
    Elementos.configurar(request.form.get('numero'))
    return redirect(url_for("home"))     