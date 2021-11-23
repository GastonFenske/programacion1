from flask import blueprints, redirect, render_template, url_for, Blueprint, current_app, request, flash
from main.forms import PerfilForm
from .bolsones import traer_bolsones
import requests, json
from flask_login import current_user
from main.routes.auth import BearerAuth
from .bolsones import cargar_productos_de_un_bolson

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente.route('/bolsones-venta/<int:page>')
def bolsones_venta(page):

    bolsones, page, pages = traer_bolsones(page)

    return render_template('clientehome.html', bg_color = 'bg-secondary', title='Bolsones Store', page = page, pages = pages, bolsones = bolsones)

@cliente.route('/compras')
def compras():

    data = {
        "usuarioId": current_user.id
    }   

    r = requests.get(f'{current_app.config["API_URL"]}/compras', headers={"content-type": "applications/json"}, json=data, auth= BearerAuth(str(request.cookies['access_token'])))

    #print(json.loads(r.text)["compras"])
    compras = json.loads(r.text)["compras"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]

    return render_template('compras.html', bg_color = 'bg-secondary', tittle= 'Mis compras', compras = compras, page = page, pages = pages)
    #return '<h1>tamo chelo<h1>'


@cliente.route('/ver-compra/<id>')
def compra(id):

    r = requests.get(f'{current_app.config["API_URL"]}/compra/{id}', headers={"content-type": "applications/json"}, json={}, auth= BearerAuth(str(request.cookies['access_token'])))

    compra = json.loads(r.text)
    print(compra)
    print(compra['bolson']['imagen'], 'La imagen de este bolson')

    json_api = {
	    "bolsonId": compra['bolson']['id']
    }

    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = json_api)

    productos = json.loads(r.text)["productosbolsones"]
    print(r.status_code)
    print(productos, 'Los productos de esta compra')

    return render_template('vercompra.html', bg_color = 'bg-secondary', title='Bolsones Store', compra = compra, productos = productos)



def cargar_un_perfil(id: int):
    form = PerfilForm()
    if not form.is_submitted():
        r = requests.get(
            f'{current_app.config["API_URL"]}/usuario/{int(id)}',
            headers={"content-type": "application/json"},
            auth=BearerAuth(str(request.cookies['access_token']))
        )
    try:
        usuario = json.loads(r.text)
        form.nombre.data = usuario['nombre']
        form.apellido.data = usuario['apellido']
        form.telefono.data = usuario['telefono']
        form.email.data = usuario['mail']
    except:
        pass

    return form


@cliente.route('/perfil/<int:id>', methods=['POST', 'GET'])
def perfil(id):
    form = cargar_un_perfil(id)
    return render_template('editarperfil.html', bg_color = 'bg-secondary', form = form, title='Bolsones Store', id = id)

@cliente.route('/actualizar-perfil/<int:id>', methods=['POST'])
def actualizar_perfil(id):
    form = cargar_un_perfil(id)    
    usuario = {
        "nombre": form.nombre.data,
        "apellido": form.apellido.data,
        "telefono": form.telefono.data,
        "mail": form.email.data
    }
    r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = usuario, auth=BearerAuth(str(request.cookies['access_token'])))

    data = {
        "current_password": form.current_password.data,
        "new_password": form.new_password.data
    }
    if form.new_password.data != '':
        r_password = requests.post(
            f'{current_app.config["API_URL"]}/auth/change-password/{id}',
            headers = {"content-type": "application/json"},
            json = data
        )
        if r_password.status_code == 401:
            flash('La contraseña actual ingresada no es correcta', 'danger')
            return redirect(url_for('cliente.perfil', id = id))
        elif r_password.status_code == 201:
            flash('La contraseña fue actualizada satisfactoriamente', 'success')

    if r.status_code == 201:
        flash('Los datos del perfil fueron actualizados satisfactoriamente', 'info')
        return redirect(url_for('cliente.perfil', id = id))


@cliente.route('/reservar-bolson/<int:id>')
def reservar_bolson(id):
    pass