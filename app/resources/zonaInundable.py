from flask import redirect, render_template, request, url_for, session
from sqlalchemy import exc

from app.models.ordenacion import Ordenacion
from app.models.puntoEncuentro import PuntoEncuentro
from app.helpers.auth import assert_permission
from app.db import db
from app.models.elementos import Elementos

def index():
    return render_template("zona_inundable/index.html")

def show(id_zona):
    return render_template("zona_inundable/show.html")

def importar():
    pass

def destroy(id_zona):
    pass