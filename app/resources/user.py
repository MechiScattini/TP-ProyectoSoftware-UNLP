from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from sqlalchemy import exc
from app.models.user import User
from app.helpers.auth import authenticated
from app.db import db
from werkzeug.security import check_password_hash, generate_password_hash

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    if request.method == "GET":
        users = db.session.query(User).all()
        return render_template("user/index.html", users=users)

    if request.method == "POST":
        q = request.form["q"]
        users_con_nombre = db.session.query(User).filter(User.username == q)
        return render_template("user/index.html", users=users_con_nombre)


def edit(user_id):
    if not authenticated(session):
        abort(401)
    user = db.session.query(User).get(user_id)
    if request.method == 'POST':
        params = request.form   
        error = None
        if not params["first_name"]:
            error = 'nombre es requerido' 
        elif not params["last_name"]:
            error = 'apellido es requerido'  
        elif not params["email"]:
            error = 'email es requerido'
        elif not params["username"]:
            error = 'nombre de usuario es requerido'
        elif '@' not in params["email"]:
             error = 'ingrese un email valido'
        if error is None:
            try:
                user.email =params['email'] #falta chequear que sea un email valido
                user.username =params['username']
                user.first_name =params['first_name']
                user.last_name =params['last_name']
                if params["bloqueado"] == 1:
                    user.bloqueado = 1
                else:
                    user.bloqueado = 0 #no funciona 
                db.session.commit()        
            except exc.IntegrityError as e:
                if 'email' in e.orig.args[1]:
                    flash("ya existe usuario con ese email")
                elif 'username' in e.orig.args[1]:
                    flash("ya existe usuario con ese nombre de usuario")
                db.session.rollback()
                return render_template("user/edit.html", user=user) 
            except ValueError as e:
                flash(e)
                db.session.rollback()
                return render_template("user/edit.html", user=user)
            flash("Usuario actualizado")
            return redirect(url_for("user_index"))
        else:
            flash(error)
            return render_template("user/edit.html", user=user)
    return render_template('user/edit.html', user= user)


def create():
    """ Creacion de usuarios """
    if not authenticated(session):
        abort(401)
    if request.method == "GET":
        return render_template("user/new.html")

    if request.method == "POST":
        params = request.form   
        error = None
        if not params["username"]:
            error = 'Nombre de usuario es requerido'
        if not params["email"]:
            error = 'Email de usuario es requerido'
        elif not params["password"]:
            error = 'Contraseña es requerido' 
        elif '@' not in params["email"]:
            error = 'ingrese un email valido' 
    
    #Chequeos de uusername y email unicos 
        email_en_db = db.session.query(User).filter(User.email==params["email"]).first()
        username_en_db= db.session.query(User).filter(User.username==params["username"]).first()
        if email_en_db is not None:
            error = 'Email {} se encuentra registrado.'.format(params["email"])
        if username_en_db is not None:
            error = 'nombre de usuario {} se encuentra registrado.'.format(params["username"])
        if error is None:
            new_user = User(**request.form)
            new_user.password = generate_password_hash(params["password"])
            db.session.add(new_user)
            db.session.commit()
            flash("Usuario agregado con exito")
            return redirect(url_for("user_create"))
        else:
            flash(error)
            return redirect(url_for("user_create"))

def delete(user_id):
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado")
    return redirect(url_for("user_index"))

