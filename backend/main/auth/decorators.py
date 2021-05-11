from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Only admins can access', 403
    return wrapper

def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'proveedor':
            return fn(*args, **kwargs)
        else:
            return 'Only proveedores can access', 403
    return wrapper

def proveedor_or_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'proveedor' or claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Only admins or proveedores can access', 403
    return wrapper

def cliente_or_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'cliente' or claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Only admins or clientes can access', 403
    return wrapper

def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == 'cliente':
            return fn(*args, **kwargs)
        else:
            return 'Only cliente can accesss', 403
    return wrapper

@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario.id

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'role': usuario.role,
        'id': usuario.id,
        'mail': usuario.mail
    }
    return claims