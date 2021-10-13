from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from sqlalchemy import exc
from sqlalchemy.sql.expression import false
from app.models.user import Rol, User, users_roles,Rol
from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.helpers.auth import authenticated, check_permission
from app.db import db
from werkzeug.security import check_password_hash, generate_password_hash

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    if request.method == "GET":

        user = db.session.query(User).filter(User.email==session['user'])
        # if not check_permission(user[0].id, 'user_index'):
        #     abort(401) 

        #users = db.session.query(User).all()
        orden = Ordenacion.query.filter_by(id=1).first()
        elem = Elementos.query.filter_by(id=1).first()
        if elem is not None:
            per_page = int(elem.cant)
        page  = int(request.args.get('page', 1))
        #aca defino por default 2 crioterios de ordenacion, por mail o descripcion
        if orden.id_orden == 1:
            users = db.session.query(User).order_by(User.email).paginate(page,per_page,error_out=False)
        else:   
            users = db.session.query(User).order_by(User.first_name).paginate(page,per_page,error_out=False) 
        return render_template("user/index.html", users=users)

    if request.method == "POST":
        q = request.form["q"]
        users_con_nombre = db.session.query(User).filter(User.username == q)
        return render_template("user/index.html", users=users_con_nombre)

def bloqueados():
    user = db.session.query(User).filter(User.email==session['user'])
    if not check_permission(user[0].id, 'user_index'):
        abort(401) 

    users =  db.session.query(User).filter(User.bloqueado == True)
    return render_template("user/index.html", users=users)

def no_bloqueados():
    user = db.session.query(User).filter(User.email==session['user'])
    if not check_permission(user[0].id, 'user_index'):
        abort(401) 

    users =  db.session.query(User).filter(User.bloqueado == False)
    return render_template("user/index.html", users=users)

def edit(user_id):
    """ Edicion de usuarios """
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
                cheackbox = None
                cheackbox = params.get("bloqueado")
                if cheackbox is not None:
                        if user.bloqueado == False:
                            rol_admin = db.session.query(Rol).filter(Rol.name =="administrador").first()
                            roles = []
                            for rol in user.roles:
                                roles.append(rol.id)
                            if  rol_admin.id not in roles:
                                user.bloqueado= True
                            else:
                                error="no puede bloquear a un administrador"
                        else:
                            user.bloqueado= False
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
            flash(error)
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
