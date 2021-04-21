from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel


class BolsonVenta(Resource):
    def get(self, id):
        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        if bolsonventa.aprobado == 1:
            return bolsonventa.to_json()
        else:
            return '', 404

class BolsonesVenta(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1).all()
        return jsonify({'bolsonesventa': [bolson.to_json() for bolson in bolsones] })
