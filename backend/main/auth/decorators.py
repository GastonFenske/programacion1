import functools
from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def role_required(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            #Verificar que el JWT es correcto
            verify_jwt_in_request()
            #Obtengo los claims
            claims = get_jwt()
            #Verificar que el rol sea uno de los permitidos por la ruta
            if claims['role'] in roles:
                #Ejecuto la funcion
                return function(*args, **kwargs)
            else:
                return 'Rol not allowed', 403
        return wrapper
    return decorator

@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return {
        'usuarioId': usuario.id,
        'role': usuario.role
    }

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'id': usuario.id,
        'role': usuario.role,
        'mail': usuario.mail
    }
    return claims