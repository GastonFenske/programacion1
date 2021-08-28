from flask import render_template, Blueprint

proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')

@proveedor.route('/home')
def home():
    return render_template('homeproveedor.html', title="Proveedor", bg_color="bg-primary")