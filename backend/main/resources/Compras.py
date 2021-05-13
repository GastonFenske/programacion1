from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import admin_required, cliente_or_admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity


class Compra(Resource):
    @cliente_or_admin_required
    def get(self, id):
        current_user = get_jwt_identity()
        try:
            compra = db.session.query(CompraModel).get_or_404(id)
            if current_user['usuarioId'] == compra.usuarioId or current_user['role'] == 'admin':
                return compra.to_json()
            else:
                return 'Unauthorized', 401
        except:
            return '', 404

    @admin_required
    def put(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        try:
            db.session.add(compra)
            db.session.commit()
            return compra.to_json(), 201
        except:
            return '', 404

    @admin_required
    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        try:
            db.session.delete(compra)
            db.session.commit()
            return '', 204
        except:
            return '', 404

class Compras(Resource):
    @admin_required
    def get(self):
        page = 1
        per_page = 10
        compras = db.session.query(CompraModel)  
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == "usuarioId":
                    compras = compras.filter(CompraModel.usuarioId == value)
                elif key == "bolsonId":
                    compras = compras.filter(CompraModel.bolsonId == value)
                elif key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)

        compras = compras.paginate(page, per_page, True, 30)

        return jsonify({
            'compras': [compra.to_json() for compra in compras.items],
            'total': compras.total,
            'pages': compras.pages,
            'page': page
        })
        
    @jwt_required()
    def post(self):
        compra = CompraModel.from_json(request.get_json())
        current_user = get_jwt_identity()
        compra.usuarioId = current_user
        try:
            db.session.add(compra)
            db.session.commit()
        except:
            return 'Esto no anda', 404
        return compra.to_json(), 201