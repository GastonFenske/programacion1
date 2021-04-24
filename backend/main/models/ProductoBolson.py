from .. import db
from . import ProductoModel, BolsonModel

class ProductoBolson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productoId = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    producto = db.relationship('Producto', back_populates="productosbolsones", uselist=False, single_parent=True)
    bolsonId = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates="productosbolsones", uselist=False, single_parent=True)

    def __repr__(self):
        return f'Producto-Bolsones: {self.id}, {self.producto.to_json()}, {self.bolson.to_json()}'

    def to_json(self):
        productobolson_json = {
            'id': self.id,
            'producto': self.producto.to_json(),
            'bolson': self.bolson.to_json()
        }
        return productobolson_json

    @staticmethod
    def from_json(producto_json):
        id = producto_json.get('id')
        productoId = producto_json.get('productoId')
        bolsonId = producto_json.get('bolsonId')
        return ProductoBolson(
            id = id,
            productoId = productoId,
            bolsonId = bolsonId
        )
