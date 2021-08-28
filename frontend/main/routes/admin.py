from flask import render_template, Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/home')
def home():
    return render_template('homeadmin.html', title='Admin', bg_color="bg-dark")

@admin.route('/agregar-proveedor')
def agregar_proveedor():

    return render_template('agregar_proveedor.html', title='Admin', bg_color="bg-dark")