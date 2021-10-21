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
    elem = Elementos.get_elementos()
    ordenPuntos = Ordenacion.get_ordenacion_puntos()
    ordenUsuarios = Ordenacion.get_ordenacion_usuarios()
    colores = Colores.get_colores()
    color = colores.privado
    return render_template("config.html", cant = elem, ordenP = ordenPuntos.orderBy, ordenU = ordenUsuarios.orderBy, coloresPriv = colores.privado, coloresPub = colores.publico, color = color)


def configurado():
    #Acá actualizo en la bd los nuevos valores ingresados
    Colores.configurar(request.form.get('colorPri'),request.form.get('colorPub'))
    Ordenacion.configurarOrdenUsuarios(request.form.get('orden_usuarios'))
    Ordenacion.configurarOrdenPuntos(request.form.get('orden_puntos'))    
    Elementos.configurar(request.form.get('numero'))
    return redirect(url_for("home"))     