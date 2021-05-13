from flask.globals import current_app
from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel
from main.auth.decorators import admin_required, cliente_required, cliente_or_admin_required 
from flask_jwt_extended import jwt_required, get_jwt_identity


class Cliente(Resource):
    @admin_required
    def get(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        if cliente.role == 'cliente':
            try:
                return cliente.to_json()
            except:
                return '', 404
        else:
            return 'cliente not found', 404

    @cliente_or_admin_required
    def delete(self, id):
        current_user = get_jwt_identity()
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        if cliente.role == 'cliente':
            if current_user['usuarioId'] == cliente.id or current_user['role'] == 'admin':
                try:
                    db.session.delete(cliente)
                    db.session.commit()
                    return '', 204
                except:
                    return '', 404
            else:
                return 'Unauthorized', 401
        else:
            return 'cliente not found', 404

    @cliente_required
    def put(self, id):
        current_user = get_jwt_identity()
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        if cliente.role == 'cliente':
            if current_user['usuarioId'] == cliente.id:
                data = request.get_json().items()
                for key, value in data:
                    setattr(cliente, key, value)
                try:
                    db.session.add(cliente)
                    db.session.commit()
                    return cliente.to_json(), 201
                except:
                    return '', 404
            else:
                return 'Unauthorized', 401
        else:
            return 'cliente not found', 404

class Clientes(Resource):
    @admin_required
    def get(self):
        page = 1
        per_page = 10
        
        clientes = db.session.query(UsuarioModel).filter(UsuarioModel.role == 'cliente')
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        clientes = clientes.paginate(page, per_page, True, 30)
        return jsonify({
            'clientes': [cliente.to_json() for cliente in clientes.items],
            'total': clientes.total,
            'pages': clientes.pages,
            'page': page
        })


    def post(self):
        cliente = UsuarioModel.from_json(request.get_json())
        cliente.role = 'cliente'
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201