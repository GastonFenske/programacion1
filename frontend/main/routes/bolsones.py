from flask import redirect, render_template, url_for, Blueprint, current_app
import requests, json

bolsones = Blueprint('bolsones', __name__, url_prefix='/bolsones')


@bolsones.route('/venta/<int:page>')
def venta(page):

    page = {
        "page": int(page)
    }

    r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"}, json=page)

    bolsones = json.loads(r.text)["bolsonesventa"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]

    return render_template('bolsoneshome.html', bg_color='bg-secondary', title='Bolsones', bolsones = bolsones, page = page, pages = pages)

@bolsones.route('/ver/<int:id>')
def ver(id):

    r = requests.get(f'{current_app.config["API_URL"]}/bolson-venta/{id}', headers={"content-type": "applications/json"}, json={})

    bolson = json.loads(r.text)
    bolsonId = bolson["id"]
    nombre = bolson["nombre"]
    fecha = bolson["fecha"]
    imagen = bolson["imagen"]
    descripcion = bolson["descripcion"]

    json_api = {
	    "bolsonId": int(id)
    }

    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = json_api)


    productos = json.loads(r.text)["productosbolsones"]

    return render_template('verbolson.html', title = f'{nombre}', bg_color = "bg-secondary", 
    nombre = nombre, imagen = imagen, descripcion = descripcion, productos = productos
    )


