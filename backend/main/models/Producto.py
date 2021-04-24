from .. import db
from . import ProveedorModel

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    proveedorId = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    proveedor = db.relationship('Proveedor', back_populates="productos", uselist=False, single_parent=True)
    productosbolsones = db.relationship("ProductoBolson", back_populates="producto", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Producto: {self.nombre}'
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': self.nombre,
            'proveedor': self.proveedor.to_json()
        }
        return producto_json
    
    @staticmethod
    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        proveedorId = producto_json.get('proveedorId')
        return Producto(
            id = id,
            nombre = nombre,
            proveedorId = proveedorId
        )    