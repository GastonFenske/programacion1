from flask_restful import Resource
from flask import request

PROVEEDORES = {
    0: {'nombreProveedor': 'proveedorTipo1'},
    1: {'nombreProveedor': 'proveedorTipo2'},
    2: {'nombreProveedor': 'proveedorTipo3'}
}

class Proveedor(Resource):
    def get(self, id):
        if int(id) in PROVEEDORES:
            return PROVEEDORES[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            data = request.get_json()
            proveedor.update(data)
            return proveedor, 201
        return '', 404

class Proveedores(Resource):
    def get(self):
        return PROVEEDORES

    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201