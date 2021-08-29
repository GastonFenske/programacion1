from .. import db
#from . import ProveedorModel
#from . import UsuarioModel

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(200), nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates="productos", uselist=False, single_parent=True)
    productosbolsones = db.relationship("ProductoBolson", back_populates="producto", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Producto: {self.nombre}'
    def to_json(self):
        producto_json = {
            'id': self.id,
            'nombre': self.nombre,
            'imagen': self.imagen,
            'usuario': self.usuario.to_json()
        }
        return producto_json
    
    @staticmethod
    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        imagen = producto_json.get('imagen')
        usuarioId = producto_json.get('usuarioId')
        return Producto(
            id = id,
            nombre = nombre,
            imagen = imagen,
            usuarioId = usuarioId
        )    