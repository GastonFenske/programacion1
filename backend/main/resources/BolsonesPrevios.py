from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
import datetime as dt
import re 

def filtrar_bolson_previo(bolson):
            #Traigo la fecha del bolson que estoy iterando            
            bolsondate = bolson.fecha

            #Como me trae todos los datos del objeto, filtro con una expresion regular para obtener solo el formato YYYY/MM/DD
            filter_date = re.findall(r'([0-9]*)-([0-9]*)-([0-9]*)', str(bolsondate), re.IGNORECASE)

            #Convierto la tupla que me devuelve la expresion regular en un str
            date_str = f"{filter_date[0][0]}-{filter_date[0][1]}-{filter_date[0][2]}"

            #Convierto lo que acabo de filtrar en un objeto python tipo datetime, para poder acceder a su atributo dia, DD
            bolson_date_object = dt.datetime.strptime(date_str, '%Y-%m-%d')

            #Obtengo la fecha actual
            today_date = dt.datetime.now()
            
            #Obtengo el atributo fecha del bolson que estoy iterando
            last_day = bolson_date_object.day
            
            #Hago la cuenta para ver si el bolson es de la semana pasada, restando el dia de hoy con el dia del bolson iterado
            calc = today_date.day - last_day
            
            #Compruebo que el bolson sea de la semana pasada
            if calc >= 7:
               return bolson

class BolsonPrevio(Resource):
    def get(self, id):
        bolsonprevio = db.session.query(BolsonModel).get_or_404(id)
        if filtrar_bolson_previo(bolsonprevio) is not None:
            return filtrar_bolson_previo(bolsonprevio).to_json()
        else:
            return '', 404


class BolsonesPrevios(Resource):
    def get(self):
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1).all()

        bolsonesprevios = []

        for bolson in bolsones:

            if filtrar_bolson_previo(bolson) is not None:
                bolsonesprevios.append(filtrar_bolson_previo(bolson))         

        
        return jsonify({'bolsonesprevios': [bolsonprevio.to_json() for bolsonprevio in bolsonesprevios] })
