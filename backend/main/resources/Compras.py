from flask_restful import Resource
from flask import request

COMPRAS = {
    0: {'nombreCompra': 'compraTipo1'},
    1: {'nombreCompra': 'compraTipo2'},
    2: {'nombreCompra': 'compraTipo3'}
}

class Compra(Resource):
    def get(self, id):
        if int(id) in COMPRAS:
            return COMPRAS[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in COMPRAS:
            compra = COMPRAS[int(id)]
            data = request.get_json()
            compra.update(data)
            return compra, 201
        return '', 404

    def delete(self, id):
        if int(id) in COMPRAS:
            del COMPRAS[int(id)]
            return '', 204
        return '', 404

class Compras(Resource):
    def get(self):
        return COMPRAS

    def post(self):
        compra = request.get_json()
        id = int(max(COMPRAS.keys())) + 1
        COMPRAS[id] = compra
        return COMPRAS[id]