from .. import login_manager
from flask import request, flash, redirect, url_for
from flask_login import UserMixin, LoginManager, current_user
import jwt
import requests

class User(UserMixin):
    def __init__(self, id, email, role):
        self.id = id
        self.email = email
        self.role = role

@login_manager.request_loader
def load_user(request):
    if 'access_token' in request.cookies:
        try:
            jwt_options = {
                'verify_signature': False,
                'verify_exp': True,
                'verify_nbf': False,
                'verify_iat': True,
                'verify_aud': False
            }
            token = request.cookies['access_token']
            data = jwt.decode(token, options=jwt_options, algorithms=["HS256"])
            user = User(data["id"], data["mail"], data["role"])
            return user
        except jwt.exceptions.InvalidTokenError:
            print('Invalid Token')
        except jwt.exceptions.DecodeError:
            print('Decode Error')
    return None

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe iniciar sesion para continuar', 'warning')
    return redirect(url_for('main.login'))

def admin_required(fn):
    def wrapper(*args, **kwargs):
        if not current_user.role == 'admin':
            return redirect(url_for('bolsones.venta', page=1))
        else:
            return fn(*args, **kwargs)
    return wrapper

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r 