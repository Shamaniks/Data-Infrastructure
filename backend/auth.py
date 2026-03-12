import jwt
import datetime
from functools import wraps
from flask import request, current_app
from responses import error
from database import db

ROLE_MAPPING = {
    'Кассир': 'cashier',
    'Старший кассир': 'worker',
    None: 'client'
}

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token: 
            return error("NO_TOKEN")
        
        try:
            # Обработка 'Bearer <token>' или просто '<token>'
            token_clean = token.split(" ")[1] if " " in token else token
            data = jwt.decode(
                token_clean, 
                current_app.config['SECRET_KEY'], 
                algorithms=["HS256"]
            )
            request.user_role = data['role']
            request.user_login = data['user']
        except Exception:
            return error("INVALID_TOKEN")
            
        return f(*args, **kwargs)
    return decorated

def create_token(login, role):
    payload = {
        'user': login,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'])

def authenticate_user(login, password):
    """Checks DB and returns (token, role, job_title) or None"""
    with db.get_cursor(db_user=db.root_user, db_pass=db.root_password) as cur:
        query = """
            SELECT p.login, jt.job_title_name
            FROM profile p
            LEFT JOIN worker w ON p.login = w.login
            LEFT JOIN job_title jt ON w.job_title_id = jt.job_title_id
            WHERE p.login = %s AND p.password = %s
        """
        cur.execute(query, (login, password))
        user = cur.fetchone()

    if not user:
        return None

    role = ROLE_MAPPING.get(user['job_title_name'], 'worker')
    
    token = jwt.encode({
        'user': user['login'],
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    return {
        "token": token,
        "role": role,
        "identity": user['job_title_name'] or "Client"
    }
