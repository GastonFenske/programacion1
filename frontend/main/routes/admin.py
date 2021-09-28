from flask import redirect, render_template, url_for, Blueprint, current_app, request
import requests, json 
from flask_login import current_user, login_required, LoginManager
from .auth import admin_required
from main.forms import PerfilForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/home')
@login_required
def home():
    return render_template('homeadmin.html', title='Admin', bg_color="bg-dark")

@admin.route('/agregar-proveedor')
def agregar_proveedor():

    page = {
        "page": 1
    }
    r = requests.get(f'{current_app.config["API_URL"]}/usuarios', headers={"content-type": "application/json"}, json=page, auth=BearerAuth(str(request.cookies['access_token'])))

    usuarios = json.loads(r.text)["usuarios"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]


    return render_template('agregar_proveedor.html', title='Admin', bg_color="bg-dark", usuarios = usuarios, page = page, pages = pages)
    #return render_template('pruebas.html', title='Admin', bg_color='bg-dark')

@admin.route('/add-proveedor/<int:id>')
def add_proveedor(id):

    json = {
        'role': 'proveedor'
    }

    r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = json, auth=BearerAuth(str(request.cookies['access_token'])))
    return redirect(url_for('admin.agregar_proveedor'))

@admin.route('/remove-proveedor/<int:id>')
def remove_proveedor(id):
    json = {
        'role': 'cliente'
    }
    r = requests.put(f'{current_app.config["API_URL"]}/usuario/{id}', headers={"content-type": "application/json"}, json = json, auth=BearerAuth(str(request.cookies['access_token'])))
    return redirect(url_for('admin.agregar_proveedor'))

    

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r 


@admin.route('/perfil')
def editar_perfil():
    form = PerfilForm()
    return render_template('editarperfiladmin.html', title='Admin', bg_color='bg-dark', form = form)

@admin.route('/bolsones')
def bolsones():

    return render_template('verbolsonesadmin.html', bg_color = 'bg-dark')
