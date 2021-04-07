from flask_restful import Resource
from flask import request

BOLSONES = {
    0: {'nombreBolson': 'bolsonTipo1'},
    1: {'nombreBolson': 'bolsonTipo2'},
    2: {'nombreBolson': 'bolsonTipo3'}
}

#Recurso bolson
class Bolson(Resource):
    #Para obtener recurso
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404

#Recurso Bolsones
class Bolsones(Resource):
    #Para obtener la lista de recursos
    def get(self,):
        return BOLSONES