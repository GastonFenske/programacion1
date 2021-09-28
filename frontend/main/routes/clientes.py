from flask import blueprints, redirect, render_template, url_for, Blueprint, current_app, request

cliente = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente.route('/ver-compra/<id>')
def compra(id):

    return render_template('vercompra.html', bg_color = 'bg-secondary')