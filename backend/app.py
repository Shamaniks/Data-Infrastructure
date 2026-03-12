from flask import Flask, jsonify
from database import db

app = Flask(__name__)
app.json.ensure_ascii = False # Cuz data has cyrillic
app.json.mimetype = "application/json; charset=utf-8"
app.json.sort_keys = False

@app.route('/api/health', methods=['GET'])
def health_check():
    """Checking API is breathing at least"""
    return jsonify({"status": "ok", "message": "Flask is running"}), 200

@app.route('/api/test-db', methods=['GET'])
def test_db():
    """Checking connection to MySQL"""
    try:
        with db.get_cursor() as cur:
            cur.execute("SELECT login, surname FROM profile LIMIT 1")
            user = cur.fetchone()
            return jsonify({
                "database_connected": True,
                "first_user_from_db": user
            }), 200
    except Exception as e:
        return jsonify({
            "database_connected": False, 
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
