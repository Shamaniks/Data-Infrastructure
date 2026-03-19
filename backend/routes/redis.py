from typing import Any, Dict
from flask import Blueprint, request
from auth import auth_required
from redis_engine.cart import CartService
import responses as res

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
@auth_required
def add_to_cart(product_id: int) -> Any:
    user_login: str = request.user_login
    quantity: int = request.args.get('quantity', 1, type=int)
    
    result: Dict[str, Any] = CartService.add_product(user_login, product_id, quantity)
    
    if "error" in result:
        return res.error(result["error"], 400)
    return res.success(result)

@cart_bp.route('/<int:product_id>', methods=['POST'])
@auth_required
def update_cart_item(product_id: int) -> Any:
    user_login: str = request.user_login
    quantity: int = request.args.get('quantity', 0, type=int)
    
    result = CartService.update_quantity(user_login, product_id, quantity)
    return res.success(result)

@cart_bp.route('/<int:product_id>', methods=['DELETE'])
@auth_required
def remove_from_cart(product_id: int) -> Any:
    user_login: str = request.user_login
    result = CartService.remove_product(user_login, product_id)
    return res.success(result)

@cart_bp.route('/', methods=['GET'])
@auth_required
def get_user_cart() -> Any:
    user_login: str = request.user_login
    result = CartService.get_cart(user_login)
    return res.success(result)
