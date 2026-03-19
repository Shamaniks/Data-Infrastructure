import jwt
import datetime
from typing import Dict, Any, Optional, Callable, Union
from flask import request, current_app, Response
from functools import wraps

import connectors
from redis_engine.auth import store_session, is_token_valid, invalidate_session

# Role mapping const
# TODO translate db content to eng, (?) add code names for roles
ROLE_MAPPING: Dict[Optional[str], str] = {
    'Кассир': 'cashier',
    'Старший кассир': 'worker',
    None: 'client'
}

def auth_required(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def decorated(*args: Any, **kwargs: Any) -> Any:
        auth_header: Optional[str] = request.headers.get('Authorization')
        if not auth_header:
            return error_res("NO_TOKEN", 401)
       
        try:
            token: str = auth_header.split(" ")[1] if " " in auth_header else auth_header
            
            data: Dict[str, Any] = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=["HS256"]
            )
            login: str = data['user']
            role: str = data['role']
            
            if not is_token_valid(login, token):
                return error_res("TOKEN_REVOKED", 401)
            
            setattr(request, 'user_role', role)
            setattr(request, 'user_login', login)
            
        except jwt.ExpiredSignatureError:
            return error_res("TOKEN_EXPIRED", 401)
        except Exception:
            return error_res("INVALID_TOKEN", 401)
           
        return f(*args, **kwargs)
    return decorated

def authenticate_user(login: str, password: str) -> Optional[Dict[str, str]]:
    """Checks DB and returns auth data or None."""
    db = connectors.get_mysql()
    
    with db.get_cursor(db_user=db.root_user, db_pass=db.root_password) as cur:
        query: str = """
            SELECT p.login, jt.job_title_name
            FROM profile p
            LEFT JOIN worker w ON p.login = w.login
            LEFT JOIN job_title jt ON w.job_title_id = jt.job_title_id
            WHERE p.login = %s AND p.password = %s
        """
        cur.execute(query, (login, password))
        user: Optional[Dict[str, Any]] = cur.fetchone()
    
    if not user:
        return None
    
    # Getting role
    job_title: Optional[str] = user.get('job_title_name')
    role: str = ROLE_MAPPING.get(job_title, 'worker')
    
    # Token gen
    token: str = create_token(user['login'], role)
    
    # Redis session
    store_session(user['login'], token)
    
    return {
        "token": token,
        "role": role,
        "identity": job_title or "Client"
    }

def create_token(login: str, role: str) -> str:
    """Generates a signed JWT."""
    payload: Dict[str, Any] = {
        'user': login,
        'role': role,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=12)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
