from flask import redirect, render_template, url_for, Blueprint, current_app
from flask.globals import request
from flask.templating import render_template_string
import requests, json
from main.routes.auth import BearerAuth
from flask_login import current_user
from main.forms.bolson_form import BolsonForm

bolsones = Blueprint('bolsones', __name__, url_prefix='/bolsones')

def traer_bolsones(page: int):
    page = {
        "page": int(page)
    }
    r = requests.get(
        f'{current_app.config["API_URL"]}/bolsones-venta',
        headers={
            "content-type": "application/json"
        },
        json = page
    )
    bolsones = json.loads(r.text)["bolsonesventa"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]

    return bolsones, page, pages


@bolsones.route('/venta/<int:page>')
def venta(page):

    bolsones, page, pages = traer_bolsones(page)

    # page = {
    #     "page": int(page)
    # }

    # r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"}, json=page)

    # bolsones = json.loads(r.text)["bolsonesventa"]
    # page = json.loads(r.text)["page"]
    # pages = json.loads(r.text)["pages"]

    return render_template('bolsoneshome.html', bg_color='bg-secondary', title='Bolsones', bolsones = bolsones, page = page, pages = pages)


def cargar_productos_de_un_bolson(id: int):
    r = requests.get(f'{current_app.config["API_URL"]}/bolson-venta/{id}', headers={"content-type": "applications/json"}, json={})
    bolson = json.loads(r.text)
    data = {
        "bolsonId": int(id)
    }
    
    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = data)

    productos = json.loads(r.text)["productosbolsones"]

    return bolson, productos

@bolsones.route('/ver/<int:id>')
def ver(id):

    bolson, productos = cargar_productos_de_un_bolson(id)
    bolsonId = bolson["id"]
    nombre = bolson["nombre"]
    fecha = bolson["fecha"]
    imagen = bolson["imagen"]
    descripcion = bolson["descripcion"]


    return render_template('verbolson.html', title = f'{nombre}', bg_color = "bg-secondary", 
    nombre = nombre, imagen = imagen, descripcion = descripcion, productos = productos, id = id
    )


@bolsones.route('/eliminar/<int:id>')
def eliminar(id):
    r = requests.delete(
        f'{current_app.config["API_URL"]}/bolson-pendiente/{int(id)}',
        headers={"content-type": "application/json"},
        auth= BearerAuth(str(request.cookies['access_token']))
    )
    if r.status_code == 204:
        return redirect(url_for('admin.bolsones_venta', page = 1))

@bolsones.route('/reservar/<int:id>', methods=['POST', 'GET'])
def reservar(id: int):
    data = {
        "usuarioId": current_user.id,
        "bolsonId": id
    }
    r = requests.post(
        f'{current_app.config["API_URL"]}/compras',
        headers = {"content-type": "application/json"},
        json = data,
        auth= BearerAuth(str(request.cookies['access_token']))
    )
    if r.status_code == 201:
        return redirect(url_for('cliente.compras'))

def cargar_un_bolson(id: int, tipo_bolson: int):
    bolson = {
        1: 'bolson-pendiente',
        2: 'bolson-venta',
        3: 'bolson-previo'
    }
    form = BolsonForm()

        #Traigo los productos
    data = {
            'per_page': 10
        }

    r = requests.get(f'{current_app.config["API_URL"]}/productos', headers={"content-type": "application/json"}, json = data)
    productos = json.loads(r.text)["productos"]

    productos = [(producto['id'], producto['nombre'])  for producto in productos]
    productos.insert(0, (0, '--Seleccionar producto'))

    form.producto.choices = productos
    form.producto2.choices = productos
    form.producto3.choices = productos
    form.producto4.choices = productos
    form.producto5.choices = productos
    if not form.is_submitted():
        r = requests.get(
            f'{current_app.config["API_URL"]}/{bolson[tipo_bolson]}/{int(id)}',
            headers={"content-type": "application/json"},
            auth=BearerAuth(str(request.cookies['access_token']))
        )
    try:
        bolson = json.loads(r.text)
        form.nombre.data = bolson['nombre']
        form.descripcion.data = bolson['descripcion']
        form.imagen.data = bolson['imagen']
        form.venta.data = bolson['aprobado']



        data = {
            'bolsonId': int(id)
        }
        r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = data)

        #Tengo los productos que ya tiene ese bolson
        productos = json.loads(r.text)["productosbolsones"]
        # print(productos)
        #productos = [p['producto']['nombre'] for p in productos]

        # print(productos)
        productos_selects = [form.producto.data, form.producto2.data, form.producto3.data, form.producto4.data, form.producto5.data]

        form.producto.data = int(productos[0]['producto']['id'])
        form.producto2.data = int(productos[1]['producto']['id'])
    

        form.producto3.data = int(productos[2]['producto']['id'])
        form.producto4.data = int(productos[3]['producto']['id'])
        form.producto5.data = int(productos[4]['producto']['id'])

        # num = 0
        # for p in productos:
        #     productos_selects[num] = int(p['producto']['id'])
        #     num += 1

    except:
        pass

    return form


@bolsones.route('/editar-bolson/<int:id>')
def editar_bolson(id):
    form = cargar_un_bolson(id, 2)
    return render_template('editar_bolson.html', bg_color='bg-secondary', title='Editar Bolson', form = form)

@bolsones.route('/actualizar-bolson/<int:id>')
def actualizar_bolson(id):
    pass

