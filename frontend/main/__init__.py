import os
from flask import Flask
from dotenv import load_dotenv

def create_app():

    app = Flask(__name__)

    load_dotenv()


    from main.routes import main, admin, proveedor
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.admin.admin)
    app.register_blueprint(routes.proveedor.proveedor)

    return app