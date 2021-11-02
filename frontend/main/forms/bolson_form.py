from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField, SelectField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class BolsonForm(FlaskForm):

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

    venta = BooleanField(
        'Listo para la venta',
        # [
        #     validators.Required(message = 'Este campo es requerido')
        # ],
        default = False
    )

    producto = SelectField(
        'Seleccionar producto #1',
        [
            validators.Required(message = 'Este campo es requiredo')
        ],
        # choices = [],
        coerce=int
    )

    # cantidad_producto = IntegerField(
    #     'Cantidad',
    #     [
    #         validators.Required()
    #     ]
    # )

    producto2 = SelectField(
        'Seleccionar producto #2',
        #choices = []
        coerce=int
    )

    producto3 = SelectField(
        'Seleccionar producto #3',
        #choices = [],
        coerce=int
    )

    producto4 = SelectField(
        'Seleccionar producto #4',
        #choices = []
        coerce=int
    )

    producto5 = SelectField(
        'Seleccionar producto #5',
        #choices = []
        coerce=int
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

class BolsonFilterForm(FlaskForm):
    id = IntegerField(
        'Filtrar bolson mediante Id',
        [
            validators.Required(message = 'Este campo es requerido')
        ]
    )
    submit = SubmitField()
    