from .. import db
import datetime as dt
from . import ClienteModel, BolsonModel

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_compra = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
    retirado = db.Column(db.Boolean, default=False, nullable=False)
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente', back_populates="compras", uselist=False, single_parent=True)
    bolsonId = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates="compras", uselist=False, single_parent=True)

    def __repr__(self):
        return f'Compra: {self.id}, {self.fecha_hora_compra}, {self.retirado}, {self.cliente.to_json()}, {self.bolson.to_json()}'

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fecha_hora_compra': str(self.fecha_hora_compra),
            'retirado': self.retirado,
            'cliente': self.cliente.to_json(),
            'bolson': self.bolson.to_json()
        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = compra_json.get('fecha_hora_compra')
        retirado = compra_json.get('retirado')
        clienteId = compra_json.get('clienteId')
        bolsonId = compra_json.get('bolsonId')
        return Compra(
            id = id,
            fecha_hora_compra = fecha_hora_compra,
            retirado = retirado,
            clienteId = clienteId,
            bolsonId = bolsonId
        )