from flask_restful import Resource
from flask import request

PRODUCTOS = {
    0: {'nombreProducto': 'productoTipo1'},
    1: {'nombreProducto': 'productoTipo2'},
    2: {'nombreProducto': 'productoTipo3'}
}

class Producto(Resource):
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in PRODUCTOS:
            del PRODUCTOS[int(id)]
            return '', 204

    def put(self, id):
        if int(id) in PRODUCTOS:
            producto = PRODUCTOS[int(id)]
            data = request.get_json()
            producto.update(data)
            return producto, 201
        return '', 404

class Productos(Resource):
    def get(self):
        return PRODUCTOS

    def post(self):
        producto = request.get_json()
        id = int(max(PRODUCTOS.keys())) + 1
        PRODUCTOS[id] = producto
        return PRODUCTOS[id] , 201
            