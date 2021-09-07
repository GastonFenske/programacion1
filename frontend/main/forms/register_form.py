from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class RegisterForm(FlaskForm):

    nombre = StringField(
        'Nombre',
        [
            validators.Required(message = 'El nombre es requerido')
        ]
    )

    apellido = StringField(
        'Apellido',
        [
            validators.Required(message = 'El apellido es requrido')
        ]
    )

    telefono = IntegerField(
        'Telefono'
    )

    email = EmailField(
        'Email',
        [
            validators.Required(message = 'El email es requerido')
        ]
    )

    password = PasswordField(
        'Password',
        [
            validators.Required(message = 'La contraseña es requrida'),
            validators.EqualTo('confirm', message = 'Las contraseñas no coinciden')
        ]
    )

    confirm = PasswordField(
        'Confirmar contraseña'
    )

    submit = SubmitField(
        'Registrarse'
    )

    