from os import path, environ
from flask import Flask, render_template, g, Blueprint
from flask_session import Session
from config import config

from app import db
from app.resources import issue
from app.resources import user
from app.resources import puntoEncuentro
import logging

from app.resources import auth
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers import auth as helper_auth



logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(has_permission=helper_auth.check_permission)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index, methods=["POST", "GET"])
    app.add_url_rule("/usuarios/nuevo", "user_create", user.create, methods=["POST", "GET"])
    app.add_url_rule("/usuarios/delete<int:user_id>", "user_delete", user.delete,methods=["POST","GET"])
    app.add_url_rule("/usuarios/editar<int:user_id>", "user_edit", user.edit,methods=["POST","GET"])
    
    # Rutas de PuntosEncuentro
    app.add_url_rule("/puntosEncuentro", "puntoEncuentro_index", puntoEncuentro.index)
    app.add_url_rule("/puntosEncuentro", "puntoEncuentro_create", puntoEncuentro.create, methods=["POST"])
    app.add_url_rule("/puntosEncuentro/nuevo", "puntoEncuentro_new", puntoEncuentro.new)
    app.add_url_rule("/puntosEncuentro/editar/<int:id_punto>", "puntoEncuentro_update", puntoEncuentro.update, methods=["POST","GET"])
    app.add_url_rule("/puntosEncuentro/eliminar/<int:id_punto>", "puntoEncuentro_destroy", puntoEncuentro.destroy, methods=["POST", "GET"])

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
