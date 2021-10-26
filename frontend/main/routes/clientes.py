from flask import blueprints, redirect, render_template, url_for, Blueprint, current_app, request
from main.forms import PerfilForm
from .bolsones import traer_bolsones
import requests, json
from flask_login import current_user
from main.routes.auth import BearerAuth

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

    json_api = {
	    "bolsonId": int(id)
    }

    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = json_api)

    productos = json.loads(r.text)["productosbolsones"]

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
    return render_template('editarperfil.html', bg_color = 'bg-secondary', form = form, title='Bolsones Store')

