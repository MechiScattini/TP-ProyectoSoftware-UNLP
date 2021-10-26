from flask import redirect, render_template, request, url_for, session
from flask.helpers import flash
from sqlalchemy import exc
from app.models.user import Rol, User,Rol
from app.models.elementos import Elementos
from app.models.ordenacion import Ordenacion
from app.models.colores import Colores
from app.helpers.auth import assert_permission
from app.db import db
from werkzeug.security import generate_password_hash

# Protected resources
def index():
    """ Muestra los usuarios del sistema """
    assert_permission(session,'user_index')

    #paginacion
    page  = int(request.args.get('page', 1,type=int))

    cant_paginas = Elementos.get_elementos()

    #variable para opción de ordenación
    ordenacion = Ordenacion.get_ordenacion_usuarios()

    #color de la vista
    color = Colores.get_color_privado()

    if request.method == "GET":
        q = request.args.get("q")
        if q:
            users= User.users_por_busqueda(q,ordenacion ,page,cant_paginas)
        else:
            users = User.paginacion(ordenacion, page, cant_paginas)
        return render_template("user/index.html", users=users,color = color)
def bloqueados():
    """ Muestra los usuarios bloqueados """
    assert_permission(session,'user_index') 
    colores = Colores.query.filter_by(id=1).first()
    if colores is None:
        color = "rojo"
    else:
        color = colores.privado
    #chequeo si habia un orden creado
    orden = Ordenacion.query.filter_by(lista = 'usuarios').first()
    if orden is None:
        orden = Ordenacion("email","orden_usuarios")
    elem = Elementos.query.first()
    elem = Elementos.query.first()
    if elem is not None:
        per_page = int(elem.cant)
    else:
        per_page = 2
    page  = int(request.args.get('page', 1,type=int))

    users =  db.session.query(User).filter(User.bloqueado == True).order_by(orden.orderBy).paginate(page,per_page,error_out=False)
    return render_template("user/index.html", users=users, color = color)

def no_bloqueados():
    """ Muestra los usuarios no bloqueados """
    assert_permission(session,'user_index')
    orden = Ordenacion.query.filter_by(lista='usuarios').first()
    colores = Colores.query.filter_by(id=1).first()
    if colores is None:
        color = "rojo"
    else:
        color = colores.privado
    #chequeo si habia un orden creado
    if orden is None:
        orden = Ordenacion("email","orden_usuarios")
    elem = Elementos.query.first()
    if elem is not None:
        per_page = int(elem.cant)
    else:
        per_page = 2
    page  = int(request.args.get('page', 1,type=int))
    
    users =  db.session.query(User).filter(User.bloqueado == False).order_by(orden.orderBy).paginate(page,per_page,error_out=False)
    return render_template("user/index.html", users=users, color = color)

def edit(user_id):
    """ Edicion de usuarios """
    assert_permission(session,'user_index')
    orden = Ordenacion.query.filter_by(lista='usuarios').first()
    colores = Colores.query.filter_by(id=1).first()
    if colores is None:
        color = "rojo"
    else:
        color = colores.privado
    #chequeo si habia un orden creado
    if orden is None:
        orden = Ordenacion("email","orden_usuarios")
    elem = Elementos.query.first()
    user = db.session.query(User).get(user_id)

    if request.method == 'POST':
        params = request.form   
        error = None
        #chequeo campos invalidos
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
                user.email =params['email'] 
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
                                flash(error)
                                roles= db.session.query(Rol).all()
                                return render_template("user/edit.html", user=user, roles=roles)
                        else:
                            user.bloqueado= False
                #actualizo roles seleccionados
                user.roles.clear()
                lista_roles= request.form["roles[]"]
                for rol_id in lista_roles:
                    rol_obj= db.session.query(Rol).get(rol_id)
                    user.roles.append(rol_obj)
                db.session.commit()    

            except exc.IntegrityError as e:
                if 'email' in e.orig.args[1]:
                    flash("ya existe usuario con ese email")
                elif 'username' in e.orig.args[1]:
                    flash("ya existe usuario con ese nombre de usuario")
                db.session.rollback()
                roles= db.session.query(Rol).all()
                return render_template("user/edit.html", user=user,roles=roles) 

            except ValueError as e:
                flash(e)
                db.session.rollback()
                roles= db.session.query(Rol).all()
                return render_template("user/edit.html", user=user,roles=roles)
            flash("Usuario actualizado")
            return redirect(url_for("user_index"))
        else:
            flash(error)
            roles= db.session.query(Rol).all()
            return render_template("user/edit.html", user=user, roles=roles)
    roles= db.session.query(Rol).all()
    return render_template('user/edit.html', user= user, roles=roles, color = color)


def create():
    """ Creacion de usuarios """
    assert_permission(session,'user_create')

    if request.method == "GET":
        roles= Rol.get_roles()
        return render_template("user/new.html", roles= roles)

    if request.method == "POST":
        params = request.form   
        error = None

        #chequeo que los campos requeridos no esten vacios
        if not params["username"]:
            error = 'Nombre de usuario es requerido'
        if not params["email"]:
            error = 'Email de usuario es requerido'
        elif not params["password"]:
            error = 'Contraseña es requerido' 
        elif '@' not in params["email"]:
            error = 'ingrese un email valido' 
    
        #Chequeos de uusername y email unicos 
        if error is None:
            email_en_db = User.get_email(params["email"])
            username_en_db= User.get_username(params["username"])
            if email_en_db is not None:
                error = 'Email {} se encuentra registrado.'.format(params["email"])
            if username_en_db is not None:
                error = 'nombre de usuario {} se encuentra registrado.'.format(params["username"])

            #agrego user a base de datos
            if error is None:
                new_user = User(username=params["username"],first_name=params["first_name"], last_name=params["last_name"], email=params["email"], password=generate_password_hash(params["password"]))
            
                lista_roles= request.form["roles[]"]
                if lista_roles is not None:
                    for rol_id in lista_roles:
                        rol_obj= Rol.get_rol(rol_id)
                        new_user.roles.append(rol_obj)
                    db.session.add(new_user)
                    db.session.commit()
                    flash("Usuario agregado con exito")
                    return redirect(url_for("user_create"))                  
        flash(error)
        roles= Rol.get_roles()
        return redirect(url_for("user_create", roles = roles))

def delete(user_id):
    assert_permission(session,'user_index')
    user = db.session.query(User).get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado")
    return redirect(url_for("user_index"))

