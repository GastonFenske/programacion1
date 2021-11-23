from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class PerfilForm(FlaskForm):

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

    new_password = PasswordField(
        'Contraseña nueva',
        [
            validators.EqualTo('new_confirm', message = 'Las contraseñas no coinciden')
        ]
    )

    new_confirm = PasswordField(
        'Confirmar contraseña nueva'
    )

    current_password = PasswordField(
        'Contraseña actual'
    )

    submit = SubmitField(
        'Actualizar datos'
    )

    