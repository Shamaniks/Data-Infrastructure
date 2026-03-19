import connectors

class CartService:
    @staticmethod
    def get_cart_key(user_id: int) -> str:
        return f"cart:{user_id}"

    @staticmethod
    def create_cart(user_id: int):
        """Create empty cart for user"""
        redis = connectors.get_redis()
        key = CartService.get_cart_key(user_id)
        if not redis.exists(key):
            redis.hset(key, mapping={})
        return {"message": "Cart created successfully", "user_id": user_id}

    @staticmethod
    def add_product(user_id: int, product_id: int, quantity: int = 1):
        """Add product to cart or increase existing quantity"""
        if quantity <= 0:
            return {"error": "Quantity must be positive"}
        
        redis = connectors.get_redis()
        key = CartService.get_cart_key(user_id)
        
        current = redis.hget(key, str(product_id))
        new_qty = int(current) + quantity if current else quantity
        
        redis.hset(key, str(product_id), new_qty)
        return {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": new_qty,
            "message": "Product added to cart"
        }

    @staticmethod
    def update_quantity(user_id: int, product_id: int, quantity: int):
        """Set exact quantity. Use negative number to subtract. 0 or less = delete item"""
        redis = connectors.get_redis()
        key = CartService.get_cart_key(user_id)
        
        if quantity > 0:
            redis.hset(key, str(product_id), quantity)
            msg = "Quantity updated"
        else:
            redis.hdel(key, str(product_id))
            msg = "Product removed from cart"
        
        return {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity if quantity > 0 else 0,
            "message": msg
        }

    @staticmethod
    def remove_product(user_id: int, product_id: int):
        """Delete product from cart"""
        redis = connectors.get_redis()
        key = CartService.get_cart_key(user_id)
        redis.hdel(key, str(product_id))
        return {"message": f"Product {product_id} removed from cart", "user_id": user_id}

    @staticmethod
    def get_cart(user_id: int):
        """Return current cart"""
        redis = connectors.get_redis()
        key = CartService.get_cart_key(user_id)
        items = redis.hgetall(key)
        cart = {int(pid): int(qty) for pid, qty in items.items()}
        return {
            "user_id": user_id,
            "items": cart,
            "total_items": sum(cart.values()),
            "message": "Cart retrieved successfully"
        }
