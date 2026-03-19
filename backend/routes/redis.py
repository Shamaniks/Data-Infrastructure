from flask import Blueprint, jsonify, request

from redis_engine.cart import CartService

cart_bp = Blueprint('cart', __name__)

# TODO: Later replace with your real JWT + Redis session decorator
# For now we accept user_id from URL (protect in production)

@cart_bp.route('/create/<int:user_id>', methods=['POST'])
def create_cart(user_id):
    result = CartService.create_cart(user_id)
    return jsonify(result), 201 if "error" not in result else 400

@cart_bp.route('/add/<int:user_id>/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    quantity = request.args.get('quantity', 1, type=int)
    result = CartService.add_product(user_id, product_id, quantity)
    return jsonify(result), 200 if "error" not in result else 400

@cart_bp.route('/update/<int:user_id>/<int:product_id>', methods=['POST'])
def update_cart_item(user_id, product_id):
    quantity = request.args.get('quantity', 0, type=int)
    result = CartService.update_quantity(user_id, product_id, quantity)
    return jsonify(result), 200

@cart_bp.route('/remove/<int:user_id>/<int:product_id>', methods=['DELETE'])
def remove_from_cart(user_id, product_id):
    result = CartService.remove_product(user_id, product_id)
    return jsonify(result), 200

@cart_bp.route('/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    result = CartService.get_cart(user_id)
    return jsonify(result), 200
