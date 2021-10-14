from flask import redirect, render_template, request, url_for, session

from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.issue import Issue
from app.db import db
from sqlalchemy import update
from sqlalchemy import select
# Public resources
def index():
        orden = Ordenacion.query.filter_by(id=1).first()
        elem = Elementos.query.filter_by(id=1).first()
        if elem is not None:
            per_page = int(elem.cant)
        else:
            per_page = 2 #si todavía no se creo el objeto asigna 2 por defecto
        page  = int(request.args.get('page', 1))
        #aca defino por default 2 crioterios de ordenacion, por mail o descripcion
        if orden.id_orden == 1:
            issues = Issue.query.order_by(Issue.email).paginate(page,per_page,error_out=False)
        else:   
            issues = Issue.query.order_by(Issue.description).paginate(page,per_page,error_out=False) 
        return render_template("issue/index.html", issues=issues)
    
def new():
    return render_template("issue/new.html")


def create():
    new_issue = Issue(**request.form)

    db.session.add(new_issue)
    db.session.commit()

    return redirect(url_for("issue_index"))
def config():

    return render_template("issue/config.html")
