#from flask_restful import Resource
#from flask import request, jsonify
#from .. import db
#from main.models import ClienteModel
#
#
#class Cliente(Resource):
#    def get(self, id):
#        cliente = db.session.query(ClienteModel).get_or_404(id)
#        try:
#            return cliente.to_json()
#        except:
#            return '', 404
#
#    def delete(self, id):
#        cliente = db.session.query(ClienteModel).get_or_404(id)
#        try:
#            db.session.delete(cliente)
#            db.session.commit()
#            return '', 204
#        except:
#            return '', 404
#
#    def put(self, id):
#        cliente = db.session.query(ClienteModel).get_or_404(id)
#        data = request.get_json().items()
#        for key, value in data:
#            setattr(cliente, key, value)
#        try:
#            db.session.add(cliente)
#            db.session.commit()
#            return cliente.to_json(), 201
#        except:
#            return '', 404
#
#class Clientes(Resource):
#    def get(self):
#        page = 1
#        per_page = 10
#        
#        clientes = db.session.query(ClienteModel)
#        if request.get_json():
#            filters = request.get_json().items()
#            for key, value in filters:
#                if key == 'page':
#                    page = int(value)
#                elif key == 'per_page':
#                    per_page = int(value)
#        clientes = clientes.paginate(page, per_page, True, 30)
#        return jsonify({
#            'clientes': [cliente.to_json() for cliente in clientes.items],
#            'total': clientes.total,
#            'pages': clientes.pages,
#            'page': page
#        })
#
#
#    def post(self):
#        cliente = ClienteModel.from_json(request.get_json())
#        db.session.add(cliente)
#        db.session.commit()
#        return cliente.to_json(), 201