from flask import render_template, Blueprint, current_app, request
from flask_login import current_user
from flask.helpers import url_for
from werkzeug.utils import redirect
from main.forms import PerfilForm, ProductoForm
import requests, json
from main.routes.auth import BearerAuth
from .clientes import cargar_un_perfil

proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')

@proveedor.route('/home')
def home():
    return render_template('homeproveedor.html', title="Proveedor", bg_color="bg-primary")

@proveedor.route('/perfil/<int:id>')
def editar_perfil(id):
    form = cargar_un_perfil(id)
    return render_template('editarperfilproveedor.html', title='Proveedor', form = form, bg_color = 'bg-primary')

@proveedor.route('/agregar-producto', methods=['POST', 'GET'])
def agregar_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        producto = {
            "nombre": form.nombre.data,
            "usuarioId": current_user.id
        }
        r = requests.post(f'{current_app.config["API_URL"]}/productos', headers={"content-type": "application/json"}, json = producto, auth=BearerAuth(str(request.cookies['access_token'])))
        if r.status_code == 200:
            return redirect(url_for('proveedor.agregar_producto'))

    return render_template('agregar_producto.html', tittle='Proveedor', bg_color = 'bg-primary', form = form)