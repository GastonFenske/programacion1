from flask import render_template, Blueprint
from main.forms import PerfilForm

proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')

@proveedor.route('/home')
def home():
    return render_template('homeproveedor.html', title="Proveedor", bg_color="bg-primary")

@proveedor.route('/perfil')
def editar_perfil():
    form = PerfilForm()
    return render_template('editarperfilproveedor.html', title='Proveedor', form = form, bg_color = 'bg-primary')