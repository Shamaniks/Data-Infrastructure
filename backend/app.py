from flask import Flask
from base_routes import init_routes

from routes.redis import cart_bp
from routes.mongo import products_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'absolutly-secret-key-no-one-can-hack-it'

app.json.ensure_ascii = False
app.json.sort_keys = False

init_routes(app)

app.register_blueprint(cart_bp,     url_prefix='/api/cart')
app.register_blueprint(products_bp, url_prefix='/api/products')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
