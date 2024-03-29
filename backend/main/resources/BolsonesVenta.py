from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required


class BolsonVenta(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        if bolsonventa.aprobado == 1:
            return bolsonventa.to_json()
        else:
            return '', 404

    @role_required(roles=['admin'])
    def put(self, id):
        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        if bolsonventa.aprobado == 1:
            for key, value in data:
                setattr(bolsonventa, key, value)
            db.session.add(bolsonventa)
            db.session.commit()
            return bolsonventa.to_json(), 201
        else:
            return '', 404



class BolsonesVenta(Resource):
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 8
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1)   
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
                    
        bolsones = bolsones.paginate(page, per_page, True, 8)
        return jsonify({
            'bolsonesventa': [bolson.to_json() for bolson in bolsones.items if bolson.aprobado == 1],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })


