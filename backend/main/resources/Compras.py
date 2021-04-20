from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModel


class Compra(Resource):
    def get(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        return compra.to_json()

    def put(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201

    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204
class Compras(Resource):
    def get(self):
        filters = request.get_json().items()
        compras = db.session.query(CompraModel)

        for key, value in filters:
            if key == "clienteId":
                compras = compras.filter(CompraModel.clienteId == value)
            elif key == "bolsonId":
                compras = compras.filter(CompraModel.bolsonId == value)
        compras = compras.all()

        #compras = db.session.query(CompraModel).all()
        return jsonify({ 'compras': [compra.to_json() for compra in compras] })

    def post(self):
        compra = CompraModel.from_json(request.get_json())
        try:
            db.session.add(compra)
            db.session.commit()
        except:
            return '', 404
        return compra.to_json(), 201