from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from flask_jwt_extended import jwt_required, get_jwt_identity


class BolsonVenta(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        if bolsonventa.aprobado == 1:
            return bolsonventa.to_json()
        else:
            return '', 404

class BolsonesVenta(Resource):
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 5
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1)   
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
                    
        bolsones = bolsones.paginate(page, per_page, True, 5)
        return jsonify({
            'bolsonesventa': [bolson.to_json() for bolson in bolsones.items if bolson.aprobado == 1],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })
