import os
from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

from flask_mail import Mail

from flask_cors import CORS

api = Api()

db = SQLAlchemy()

jwt = JWTManager()

mailsender = Mail()

def create_app():

    app = Flask(__name__)

    load_dotenv()

    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.mknod(f'{PATH}{DB_NAME}')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{PATH}{DB_NAME}'
    db.init_app(app)

    #Importar los recursos
    import main.resources as resources
    api.add_resource(resources.BolsonesResource, '/bolsones')
    api.add_resource(resources.BolsonResource, '/bolson/<id>')
    api.add_resource(resources.BolsonesVentaResource, '/bolsones-venta')
    api.add_resource(resources.BolsonVentaResource, '/bolson-venta/<id>')
    api.add_resource(resources.BolsonesPendientesResource, '/bolsones-pendientes')
    api.add_resource(resources.BolsonPendienteResource, '/bolson-pendiente/<id>')
    api.add_resource(resources.BolsonesPreviosResoruce, '/bolsones-previos')
    api.add_resource(resources.BolsonPrevioResource, '/bolson-previo/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')
    api.add_resource(resources.ComprasResource, '/compras')
    api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.ProveedoresResource, '/proveedores')
    api.add_resource(resources.ProveedorResoruce, '/proveedor/<id>')
    api.add_resource(resources.ProductosBolsonesResource, '/productos-bolsones')
    api.add_resource(resources.ProductoBolsonResource, '/producto-bolson/<id>')
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')

    api.init_app(app)

    #cargar clave secreta
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    #cargar tiempo de expiracion de tokens
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import routes
    app.register_blueprint(auth.routes.auth)

    from main.mail import functions
    app.register_blueprint(mail.functions.mail)

    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')

    mailsender.init_app(app)

    #Permitir solicitudes de otros origenes
    cors = CORS(app, support_credentials=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    return app