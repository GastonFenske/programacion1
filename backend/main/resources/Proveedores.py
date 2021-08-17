from flask.globals import current_app
from flask_jwt_extended.utils import get_current_user
from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required


class Proveedor(Resource):
    @role_required(roles=['admin', 'proveedor'])
    def get(self, id):
        current_user = get_jwt_identity()
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        if proveedor.role == 'proveedor':
            if current_user['usuarioId'] == proveedor.id or current_user['role'] == 'admin':
                try:
                    return proveedor.to_json()
                except:
                    return '', 404
            else:
                return 'Unauthorized', 401
        else:
            return 'proveedor not found', 404

    @role_required(roles=['admin'])
    def delete(self, id):
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        if proveedor.role == 'proveedor':
            try:
                db.session.delete(proveedor)
                db.session.commit()
                return '', 204
            except:
                return '', 404
        else:
            return 'proveedor not found', 404

    @role_required(roles=['admin'])
    def put(self, id):
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        if proveedor.role == 'proveedor':
            data = request.get_json().items()
            for key, value in data:
                setattr(proveedor, key, value)
            try:
                db.session.add(proveedor)
                db.session.commit()
                return proveedor.to_json(), 201
            except:
                return '', 404
        else:
            return 'proveedor not found', 404

class Proveedores(Resource):
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 10
        proveedores = db.session.query(UsuarioModel).filter(UsuarioModel.role == 'proveedor')
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        proveedores = proveedores.paginate(page, per_page, True, 30)

        return jsonify({
            'proveedores': [proveedor.to_json() for proveedor in proveedores.items],
            'total': proveedores.total,
            'pages': proveedores.pages,
            'page': page
        })

    @role_required(roles=['admin'])
    def post(self):
        proveedor = UsuarioModel.from_json(request.get_json())
        proveedor.role = 'proveedor'
        try:
            db.session.add(proveedor)
            db.session.commit()
        except:
            return '', 404
        return proveedor.to_json(), 201