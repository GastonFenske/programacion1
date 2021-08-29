import os
from flask import Flask
from dotenv import load_dotenv

def create_app():

    app = Flask(__name__)

    load_dotenv()

    app.config['API_URL'] = os.getenv('API_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    from main.routes import main, admin, proveedor, bolsones
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.admin.admin)
    app.register_blueprint(routes.proveedor.proveedor)
    app.register_blueprint(routes.bolsones.bolsones)

    return app