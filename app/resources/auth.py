from flask import redirect, render_template, request, url_for, abort, session, flash
from werkzeug.security import check_password_hash

from app.models.user import User


def login():
    return render_template("auth/login.html")


def authenticate():

    params = request.form
    user = User.query.filter(
        User.email==params["email"] and User.password==params["password"]
    ).first()
    error = None
    if not user:
        error= "Usuario y/o clave incorrecto."
        return redirect(url_for("auth_login"))
    #elif not check_password_hash(user.password, params['password']):
       # error = ('Usuario y/o contraseña invalidos')

    if error is None:
        session["user"] = user.email
        flash("La sesión se inició correctamente.")
        return redirect(url_for("home"))
    
    flash(error)


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
