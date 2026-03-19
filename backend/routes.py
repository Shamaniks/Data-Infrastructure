from typing import Dict, Any, Optional
from flask import Flask, request

import connectors
from auth import auth_required, authenticate_user
import responses as res

def init_routes(app: Flask) -> None:
    @app.route('/api/health')
    def health() -> Any:
        return res.success(message="API is breathing")

    @app.route('/api/login', methods=['POST'])
    def login() -> Any:
        data: Dict[str, Any] = request.json or {}
        login_val: Optional[str] = data.get('login')
        password_val: Optional[str] = data.get('password')
        
        auth_data: Optional[Dict[str, str]] = authenticate_user(login_val, password_val)
        
        if not auth_data:
            return res.error("WRONG_CREDENTIALS")
            
        return res.success(auth_data)

    @app.route('/api/data/<table_name>', methods=['GET'])
    @auth_required
    def get_data(table_name: str) -> Any:
        """ Just get all that data from table, without join"""
        db = connectors.get_mysql()
        try:
            with db.get_cursor(db_user=request.user_role) as cur:
                # TODO fix sql-injection
                cur.execute(f"SELECT * FROM {table_name} LIMIT 100")
                return res.success(cur.fetchall())
        except Exception as e:
            return res.error("ACCESS_DENIED", details=str(e))
