from flask import redirect, render_template, request, url_for, session, flash
from app.db import db
from app.models.user import User
from app.models.colores import Colores
from werkzeug.security import check_password_hash
from app.helpers.auth_google import callback_google


def callback_control():
    user_info = callback_google()
    if user_info.json().get("email_verified"):
        users_email = user_info.json()["email"]
    else:
        return "User email not available or not verified by Google.", 400
    
    #Busco si existe un usuario en la bd con ese email
    user =User.get(users_email)
    if  user is None:

        # Doesn't exist? Add it to the database.
        new_user = User.create_with_google(user_info)

        if User.esta_en_espera(new_user.id):
            error= "Se registro el usuario exitosamente, espere a que el administrador habilite su cuenta"
            flash(error)
            return redirect(url_for("auth_login"))
        else:
             #login
            session.clear()
            session["user"] = new_user.email
            session["user2"] = new_user
    else:
        # existe ? me fijo si puede iniciar sesion
        if  User.esta_bloqueado(user.id):
            error= "Usuario bloqueado no puede iniciar sesion"
            flash(error)
            return redirect(url_for("auth_login"))
        elif  User.esta_en_espera(user.id):
            error= "Usuario en espera no puede iniciar sesion"
            flash(error)
            return redirect(url_for("auth_login"))
        else:
            #login
            session.clear()
            session["user"] = user.email
            session["user2"] = user


    # Send user back to homepage
    return redirect(url_for("home"))



def espera():
    return render_template("espera.html")


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


