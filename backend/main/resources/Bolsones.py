from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel


#Recurso bolson
class Bolson(Resource):
    #Para obtener recurso
    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()

#Recurso Bolsones
class Bolsones(Resource):
    #Para obtener la lista de recursos
    def get(self,):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])
