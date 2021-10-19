from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class ProductoForm(FlaskForm):

    nombre = StringField(
        'Nombre',
        [
            validators.Required(message = 'El nombre del producto es requerido')
        ]
    )

    submit = SubmitField(
        'Agregar producto'
    )

    