from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel



class BolsonesPendientes(Resource):
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

    def post(self):
        bolsonpendiente = BolsonModel.from_json(request.get_json())
        db.session.add(bolsonpendiente)
        db.session.commit()
        return bolsonpendiente.to_json(), 201

class BolsonPendiente(Resource):
    def get(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolsonpendiente.aprobado == 0:
            return bolsonpendiente.to_json()
        else:
            return '', 404

    def delete(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        if bolsonpendiente.aprobado == 0:
            db.session.delete(bolsonpendiente)
            db.session.commit()
            return '', 204
        else:
            return '', 404
    
    def put(self, id):
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(bolsonpendiente, key, value)
        if bolsonpendiente.aprobado == 0:
            db.session.add(bolsonpendiente)
            db.session.commit()
            return bolsonpendiente.to_json(), 201
        else:
            return '', 404