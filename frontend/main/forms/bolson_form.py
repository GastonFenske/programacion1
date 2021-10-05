from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class ProductoForm(FlaskForm):

    # def __init__(self, productos: list):
    #     self.productos = productos

    nombre = StringField(
        'Nombre del bolson',
        [
            validators.Required(message = 'El nombre es requerido')
        ]
    )

    descripcion = StringField(
        'Descripcion',
        [
            validators.Required(message = 'La descripcion es requrida')
        ]
    )

    venta = IntegerField(
        'Listo para la venta',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )

    producto = SelectField(
        'Seleccionar producto #1',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Manzanas'), ('Lentejas')]
    )

    producto2 = SelectField(
        'Seleccionar producto #2',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Manzanas'), ('Lentejas')]
    )

    producto3 = SelectField(
        'Seleccionar producto #3',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Manzanas'), ('Lentejas')]
    )

    producto4 = SelectField(
        'Seleccionar producto #4',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Manzanas'), ('Lentejas')]
    )

    producto5 = SelectField(
        'Seleccionar producto #5',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        choices = [('Seleccionar producto'), ('Manzanas'), ('Lentejas')]
    )

    imagen = StringField(
        'Imagen del bolson',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )

    submit = SubmitField(
        'Agregar bolson'
    )

    