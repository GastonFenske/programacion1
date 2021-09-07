from flask import Blueprint, redirect, url_for, render_template, current_app
from main.forms import RegisterForm, LoginForm
import requests, json


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
            return redirect(url_for('main.login'))

    return render_template('register.html', title='Register', bg_color="bg-secondary", form = form)

@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', bg_color="bg-secondary", form = form)

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))