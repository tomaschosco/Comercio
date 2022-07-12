from os import path, environ
from flask import Flask, render_template, g, request
from config import config
from app import db
from app.db_sqlachemy import db_sqlalchemy
from app.resources import product

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    app.debug=True
    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    #configure store img
    app.config["UPLOAD_FOLDER"]="static/uploads"

    # Configure db
    db.init_app(app)

    # Configure sqlAlchemy
    conf = app.config
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + \
        conf["DB_USER"]+":"+conf["DB_PASS"]+"@" + \
        conf["DB_HOST"]+"/"+conf["DB_NAME"]
    db_sqlalchemy.init_app(app)
    
    #Inicio
    app.add_url_rule("/","lista_productos",product.listado)
    #Agregar Producto (modificar)
    app.add_url_rule("/formulario","formulario_Producto",product.form)
    app.add_url_rule("/nuevo","nuevoProducto",product.nuevo, methods=["POST"])
    #Editar Producto
    app.add_url_rule("/editar/<int:id>", "producto_editar",product.editar,methods=["GET","POST"])
    #Eliminar Producto
    app.add_url_rule("/eliminar/<int:id>", "producto_eliminar", product.eliminar)
    return app