from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.functions import user
from app.models.user import User
from app.helpers.auth import authenticated
from app.db import db
from werkzeug.security import check_password_hash, generate_password_hash

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    if request.method == "POST":
        user_email =request.args.get('user_email',None)
        user = User.query.filter(User.email == user_email).first()
        db.session.delete(user)
        db.session.commit()
    users = User.query.all()
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

def edit(user_id):
    if not authenticated(session):
        abort(401)
    user = User.query.get(user_id)
    if request.method == 'POST':
        params = request.form   
        error = None

        if not params["first_name"]:
            error = 'nombre es requerido' 
        if not params["last_name"]:
            error = 'apellido es requerido'  
        if not params["email"]:
            error = 'email es requerido'
        if not params["username"]:
            error = 'nombre de usuario es requerido'

        """if user.email != params["email"]:
            email_en_db= User.query.filter(user.email == params["email"]).first()
            if email_en_db is not None:
                error = 'email {} se encuentra registrado.'.format(params["email"])
        if user.username != params["username"]:
            username_en_db= User.query.filter(user.username == params["username"]).first()
            if username_en_db is not None:
                error = 'username {} se encuentra registrado.'.format(params["username"])    """       

        if error is None:
            user.email =params['email']
            user.username =params['username']
            user.first_name =params['first_name']
            user.last_name =params['last_name']
            db.session.commit()
            flash("Usuario actualizado")
            return redirect(url_for("user_index"))
        flash(error)
    return render_template('user/edit.html', user= user)

def create():
    """ Creacion de usuarios """
    if not authenticated(session):
        abort(401)
    
    params = request.form   
    error = None
    if not params["username"]:
        error = 'Nombre de usuario es requerido'
    if not params["email"]:
        error = 'Email de usuario es requerido'
    elif not params["password"]:
        error = 'Contraseña es requerido'  
    
    #Chequeos de uusername y email unicos 
    email_en_db = User.query.filter(User.email==params["email"]).first()
    username_en_db= User.query.filter(User.username==params["username"]).first()
    if email_en_db is not None:
        error = 'Email {} se encuentra registrado.'.format(params["email"])
    if username_en_db is not None:
        error = 'nombre de usuario {} se encuentra registrado.'.format(params["username"])
    if error is None:
        new_user = User(**request.form)
        new_user.password = generate_password_hash(params["password"])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("user_index"))
    
    flash(error)
    return redirect(url_for("user_new"))

def delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado")
    return redirect(url_for("user_index"))