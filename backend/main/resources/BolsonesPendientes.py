from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required




class BolsonesPendientes(Resource):
    @role_required(roles=['admin', 'proveedor'])
    def get(self):
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 0)

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)

        return jsonify({
            'bolsonespendientes': [bolson.to_json() for bolson in bolsones.items],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })

    @role_required(roles=['admin'])
    def post(self):
        bolsonpendiente = BolsonModel.from_json(request.get_json())
        db.session.add(bolsonpendiente)
        db.session.commit()
        return bolsonpendiente.to_json(), 201

class BolsonPendiente(Resource):
    @role_required(roles=['admin', 'proveedor'])
    def get(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolsonpendiente.aprobado == 0:
            return bolsonpendiente.to_json()
        else:
            return '', 404

    @role_required(roles=['admin'])
    def delete(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolsonpendiente.aprobado == 0 or bolsonpendiente.aprobado == 1:
            db.session.delete(bolsonpendiente)
            db.session.commit()
            return '', 204
        else:
            return '', 404
    
    @role_required(roles=['admin'])
    def put(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        if bolsonpendiente.aprobado == 0:
            for key, value in data:
                setattr(bolsonpendiente, key, value)
            db.session.add(bolsonpendiente)
            db.session.commit()
            return bolsonpendiente.to_json(), 201
        else:
            return '', 404