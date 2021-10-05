from flask import blueprints, redirect, render_template, url_for, Blueprint, current_app, request
from main.forms import PerfilForm

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente.route('/home')
def home():

    return render_template('clientehome.html', bg_color = 'bg-secondary', title='Bolsones Store')

@cliente.route('/ver-compra/<id>')
def compra(id):

    return render_template('vercompra.html', bg_color = 'bg-secondary', title='Bolsones Store')


@cliente.route('/perfil')
def perfil():

    form = PerfilForm()

    return render_template('editarperfil.html', bg_color = 'bg-secondary', form = form, title='Bolsones Store')