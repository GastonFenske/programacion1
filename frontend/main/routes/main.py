from flask import Blueprint, redirect, url_for, render_template, current_app, flash, make_response, request
from main.forms import RegisterForm, LoginForm
import requests, json
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from .auth import User


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('home.html', title='Bolsones Store')

@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = {
            'nombre': form.nombre.data,
            'apellido': form.apellido.data,
            'telefono': form.telefono.data,
            'mail': form.email.data,
            'password': form.password.data
        }
        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/register', json=user
        )
        if r.status_code == 201:
            flash(f'¡Felicitaciones {user["nombre"]} te has registrado exitosamente! Por favor inicia sesion para continuar', 'success')
            return redirect(url_for('main.login'))
        elif r.status_code == 409:
            flash(f'Ya existe una cuenta creada con el email {user["mail"]}', 'info')
            return redirect(url_for('main.register'))


    return render_template('register.html', title='Register', bg_color="bg-secondary", form = form)



@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        data = {
            'mail': form.email.data,
            'password': form.password.data
        }
        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/login',
            headers={"content-type": "application/json"},
            json=data
        )
        if r.status_code == 200:
            user_data = json.loads(r.text)
            user = User(id=user_data.get('id'), email=user_data.get('mail'), role=user_data.get('role'))
            login_user(user)
            if current_user.role == 'admin':
                req = make_response(redirect(url_for('admin.home')))
            elif current_user.role == 'proveedor':
                req = make_response(redirect(url_for('proveedor.home')))
            else:
                req = make_response(redirect(url_for('cliente.bolsones_venta', page = 1)))
            req.set_cookie('access_token', user_data.get('access_token'), httponly=False)

            if current_user.is_authenticated:
                print(current_user.email, 'email del current user')
            return req
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            return redirect(url_for('main.login'))

    return render_template('login.html', title='Login', bg_color="bg-secondary", form = form)




@main.route('/logout')
def logout():
    req = make_response(redirect(url_for('main.index')))
    req.set_cookie('access_token', '', httponly = True)
    req.delete_cookie('access_token', httponly=False)
    logout_user()
    return req