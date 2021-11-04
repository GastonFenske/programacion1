from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class FilterCompraForm(FlaskForm):
    status = SelectField(
        'Filtrar compras por estado',
        [
            validators.Required(message = 'Este campo es requerido')
        ],
        coerce = int,
    )
    submit = SubmitField(
        'Filtrar'
    )