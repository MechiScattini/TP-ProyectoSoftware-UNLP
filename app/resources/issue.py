from flask import redirect, render_template, request, url_for

from app.models.issue import Issue
from app.db import db

# Public resources


def index(page):
        page = 1
        per_page = 2
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
    
    return redirect(url_for("index", per_pag = request.form["numero"]))