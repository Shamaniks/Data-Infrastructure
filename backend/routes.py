from flask import request
from database import db
from auth import auth_required, create_token, authenticate_user
import responses as res

ROLE_MAPPING = {
    'Кассир': 'cashier',
    'Старший кассир': 'worker',
    None: 'client' # If job_title is NULL (not in worker table)
}

def init_routes(app):
    @app.route('/api/health')
    def health():
        return res.success(message="API is breathing")

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.json or {}
        auth_data = authenticate_user(data.get('login'), data.get('password'))
        
        if not auth_data:
            return res.error("WRONG_CREDENTIALS")
            
        return res.success(auth_data)

    @app.route('/api/data/<table_name>', methods=['GET'])
    @auth_required
    def get_data(table_name):
        try:
            with db.get_cursor(db_user=request.user_role) as cur:
                cur.execute(f"SELECT * FROM {table_name} LIMIT 100")
                return res.success(cur.fetchall())
        except Exception as e:
            return res.error("ACCESS_DENIED", details=e)

