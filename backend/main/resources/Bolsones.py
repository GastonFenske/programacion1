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
    def get(self):

        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)

        return jsonify({
            'bolsones': [bolson.to_json() for bolson in bolsones.items],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page 
        })