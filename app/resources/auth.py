from flask import redirect, render_template, request, url_for, session, flash
from app.db import db
from app.models.user import User
from app.models.colores import Colores
from werkzeug.security import check_password_hash


def login():
    colores = Colores.query.first()
    color = "default"
    if colores is not None:
        color = colores.publico
    return render_template("auth/login.html", color = color)


def authenticate():
    
    params = request.form

    user = db.session.query(User).filter(
        User.email==params["email"]
    ).first()
    error = None
    if not user:
        user = db.session.query(User).filter(
            User.username==params["email"]
        ).first()
        if not user:
            error= "Usuario y/o clave incorrecto."
            flash(error)
            return redirect(url_for("auth_login"))

    if not check_password_hash(user.password, params["password"]):
        error= "Usuario y/o clave incorrecto."
        flash(error)
        return redirect(url_for("auth_login"))  
             
    if user.bloqueado == True:
        error= "Usuario bloqueado no puede iniciar sesion"
        flash(error)
        return redirect(url_for("auth_login"))   

    if error is None:
        session.clear()
        session["user"] = user.email
        session["user2"] = user
        flash("La sesión se inició correctamente.")
        return redirect(url_for("home"))
    


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
