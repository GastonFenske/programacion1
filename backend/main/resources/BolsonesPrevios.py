from flask_restful import Resource
from flask import request

BOLSONESPREVIOS = {
    0: {'nombreBolsonPrevio': 'bolsonPrevioTipo1'},
    1: {'nombreBolsonPrevio': 'bolsonPrevioTipo2'},
    2: {'nombreBolsonPrevio': 'bolsonPrevioTipo3'}
}

class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return '', 404

class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONESPREVIOS