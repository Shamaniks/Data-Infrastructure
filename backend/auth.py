import jwt
import datetime
from typing import Dict, Any, Optional, Callable, Union
from flask import request, current_app, Response

import connectors
from redis_engine.auth import store_session, is_token_valid, invalidate_session

# Role mapping const
# TODO translate db content to eng, (?) add code names for roles
ROLE_MAPPING: Dict[Optional[str], str] = {
    'Кассир': 'cashier',
    'Старший кассир': 'worker',
    None: 'client'
}

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
