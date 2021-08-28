from flask import Blueprint, redirect, url_for, render_template


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('home.html', title='Bolsones Store')

@main.route('/register')
def register():
    return render_template('register.html', title='Register', bg_color="bg-secondary")

@main.route('/login')
def login():
    return render_template('login.html', title='Login', bg_color="bg-secondary")

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))