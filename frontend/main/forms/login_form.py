from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class LoginForm(FlaskForm):

    email = EmailField(
        'Email',
        [
            validators.Required(message = 'El email es requerido')
        ]
    )

    password = PasswordField(
        'Password',
        [
            validators.Required(message = 'La contraseña es requrida')
        ]
    )

    submit = SubmitField(
        'Iniciar sesion'
    )

    