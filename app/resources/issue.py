from flask import redirect, render_template, request, url_for, session

from app.models.elementos import Elementos
from app.models.issue import Issue
from app.db import db
from sqlalchemy import update
from sqlalchemy import select
# Public resources
def index():
        elem = Elementos.query.filter_by(id = 1).first()
        per_page = int(elem.cant)
        page  = int(request.args.get('page', 1))
        issues = Issue.query.paginate(page,per_page,error_out=False)
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
def configurado():
    
    elem = Elementos.query.filter_by(id = 1).first()
    elem.cant = int(request.form.get('numero'))
    db.session.commit()
    return redirect(url_for("home"))