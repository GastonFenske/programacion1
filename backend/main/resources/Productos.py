from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoModel

class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        return producto.to_json()

    def delete(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204

    def put(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(), 201

class Productos(Resource):
    def get(self):
        filters = request.get_json().items()
        productos = db.session.query(ProductoModel)  

        for key, value in filters:
            if key == "clienteId":
                productos = productos.filter(CompraModel.clienteId == value)
        productos = productos.all()

        return jsonify({ 'productos': [compra.to_json() for compra in compras] })

    def post(self):
        producto = ProductoModel.from_json(request.get_json())
        try:
            db.session.add(producto)
            db.session.commit()
        except:
            return '', 404
        return producto.to_json()
            