from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoBolsonModel

class ProductosBolsones(Resource):
    def get(self):
        page = 1
        per_page = 10
        productosbolsones = db.session.query(ProductoBolsonModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
        productosbolsones = productosbolsones.paginate(page, per_page, True, 30)
        
        return jsonify({
            'productosbolsones': [productobolson.to_json() for productobolson in productosbolsones.items],
            'total': productosbolsones.total,
            'pages': productosbolsones.pages,
            'page': page
        })


    def post(self):
        productobolson = ProductoBolsonModel.from_json(request.get_json())
        db.session.add(productobolson)
        db.session.commit()
        return productobolson.to_json(), 201

class ProductoBolson(Resource):
    def get(self, id):
        productobolson = db.session.query(ProductoBolsonModel).get_or_404(id)
        try:
            return productobolson.to_json()
        except:
            return '', 404

    def delete(self, id):
        productobolson = db.session.query(ProductoBolsonModel).get_or_404(id)
        try:
            db.session.delete(productobolson)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        productobolson = db.session.query(ProductoBolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(productobolson, key, value)
        try:
            db.session.add(productobolson)
            db.session.commit()
            return productobolson.to_json(), 201
        except:
            return '', 404        