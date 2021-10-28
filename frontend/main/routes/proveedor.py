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
    return render_template('editarperfilproveedor.html', title='Proveedor', form = form, bg_color = 'bg-primary', id = id)

@proveedor.route('/actualizar-perfil/<int:id>', methods=['POST'])
def actualizar_perfil(id):
    form = cargar_un_perfil(id)
    usuario = {
        "nombre": form.nombre.data,
        "apellido": form.apellido.data,
        "telefono": form.telefono.data,
        "mail": form.email.data
    }
    r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = usuario, auth=BearerAuth(str(request.cookies['access_token'])))

    if r.status_code == 201:

        return redirect(url_for('proveedor.editar_perfil', id = id))


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
            return redirect(url_for('proveedor.ver_productos'))

    return render_template('agregar_producto.html', tittle='Proveedor', bg_color = 'bg-primary', form = form)

@proveedor.route('/ver-productos')
def ver_productos():

    data = {
        "usuarioId": current_user.id
    }

    r = requests.get(
        f'{current_app.config["API_URL"]}/productos',
        headers={"content-type": "application/json"},
        json = data,
    )

    productos = json.loads(r.text)['productos']
    pages = json.loads(r.text)['pages']
    page = json.loads(r.text)['page']

    return render_template('ver_productos_proveedor.html', bg_color = 'bg-primary', title = 'Productos Proveedor', productos = productos, page = page, pages = pages)

@proveedor.route('/eliminar-producto/<int:id>')
def eliminar_producto(id):

    r = requests.delete(
        f'{current_app.config["API_URL"]}/producto/{id}',
        headers={"content-type": "application/json"},
        auth=BearerAuth(str(request.cookies['access_token']))
    )

    if r.status_code == 204:

        return redirect(url_for('proveedor.ver_productos'))

    else:

        return f'<h1>{r.status_code}</h1>'

@proveedor.route('/editar-producto/<int:id>')
def editar_producto(id):

    form = ProductoForm()

    if not form.is_submitted():
        r = requests.get(
            current_app.config["API_URL"]+f'/producto/{id}' 
        )
        producto = json.loads(r.text)

        form.nombre.data = producto['nombre']

    return render_template('editar_producto_proveedor.html', bg_color = 'bg-primary', title = 'Editar Producto', form = form, id = id)

@proveedor.route('/actualizar-producto/<int:id>', methods=['POST'])
def actualizar_producto(id):

    form = ProductoForm()

    producto = {
        "nombre": form.nombre.data
    }

    r = requests.put(
        f'{current_app.config["API_URL"]}/producto/{id}',
        headers={"content-type": "application/json"},
        json = producto,
        auth=BearerAuth(str(request.cookies['access_token']))
    )
    if r.status_code == 201:

        return redirect(url_for('proveedor.ver_productos', id = id))