from flask_restful import Resource
from flask import request

BOLSONESPENDIENTES = {
    0: {'nombreBolsonPendiente': 'bolsonPendienteTipo1'},
    1: {'nombreBolsonPendiente': 'bolsonPendienteTipo2'},
    2: {'nombreBolsonPendiente': 'bolsonPendienteTipo3'}
}

class BolsonesPendientes(Resource):
    def get(self):
        return BOLSONESPENDIENTES

    def post(self):
        bolson_pendiente = request.get_json()
        id = int(max(BOLSONESPENDIENTES.keys())) + 1
        BOLSONESPENDIENTES[id] = bolson_pendiente
        return BOLSONESPENDIENTES[id], 201

class BolsonPendiente(Resource):
    def get(self, id):
        if int(id) in BOLSONESPENDIENTES:
            return BOLSONESPENDIENTES[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in BOLSONESPENDIENTES:
            del BOLSONESPENDIENTES[int(id)]
            return '', 204
        return '', 404
    
    def put(self, id):
        if int(id) in BOLSONESPENDIENTES:
            bolson_pendiente = BOLSONESPENDIENTES[int(id)]
            data = request.get_json()
            bolson_pendiente.update(data)
            return bolson_pendiente, 201
        return '', 404