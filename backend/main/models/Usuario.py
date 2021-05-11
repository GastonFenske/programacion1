from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido  = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=True)
    mail = db.Column(db.String(64), nullable=False, unique=False, index=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(15), nullable=False, default="cliente")
    productos = db.relationship('Producto', back_populates="usuario", cascade="all, delete-orphan")
    compras = db.relationship('Compra', back_populates="usuario", cascade="all, delete-orphan")

    @property
    def plain_password(self):
        raise ArithmeticError('Password can\'t be read')

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)

    def validate_pass(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'{self.mail}'

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'mail': self.mail,
            'role': self.role
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        mail = usuario_json.get('mail')
        password = usuario_json.get('password')
        role = usuario_json.get('role')
        return Usuario(
            id = id,
            nombre = nombre,
            apellido = apellido,
            telefono = telefono,
            mail = mail,
            plain_password = password,
            role = role
        )


