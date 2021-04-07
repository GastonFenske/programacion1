from flask_restful import Resource
from flask import request

BOLSONESVENTA = {
    0: {'nombreBolsonVenta': 'bolsonVentaTipo1'},
    1: {'nombreBolsonVenta': 'bolsonVentaTipo2'},
    2: {'nombreBolsonVenta': 'bolsonVentaTipo3'}
}

class BolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return '', 404

class BolsonesVenta(Resource):
    def get(self):
        return BOLSONESVENTA