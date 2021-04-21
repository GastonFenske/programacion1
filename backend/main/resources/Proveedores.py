from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProveedorModel


class Proveedor(Resource):
    def get(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        return proveedor.to_json()

    def delete(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204

    def put(self, id):
        proveedor = db.session.query(ProveedorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201

class Proveedores(Resource):
    def get(self):
        proveedores = db.session.query(ProveedorModel).all()
        return jsonify([proveedor.to_json() for proveedor in proveedores])

    def post(self):
        proveedor = ProveedorModel.from_json(request.get_json())
        try:
            db.session.add(proveedor)
            db.session.commit()
        except:
            return '', 404
        return proveedor.to_json(), 201