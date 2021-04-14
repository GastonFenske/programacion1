from .. import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Producto: {self.nombre}'
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': self.nombre
        }
        return producto_json
    
    @staticmethod
    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        return Producto(
            id = id,
            nombre = nombre
        )    