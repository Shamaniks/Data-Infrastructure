from flask import Blueprint, jsonify, request
from connectors import get_mongo

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    """Return product list
    
    Requests args:
      ?count=10  how many
      ?offset=0  how many to skip
    """
    # Getting default values
    try:
        limit = int(request.args.get('count', 10))
        offset = int(request.args.get('offset', 0))
        
        if limit < 1: limit = 10
        if offset < 0: offset = 0
    except ValueError:
        limit = 10
        offset = 0

    mongo = get_mongo()
    collection = mongo.get_collection("products")
    
    cursor = collection.find(
        {}, 
        {"_id": 1, "clothing_type": 1, "price": 1}
    ).skip(offset).limit(limit)
    
    products = []
    for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc["clothing_type"],
            "price": doc["price"]
        })
    
    return jsonify({
        "status": "success",
        "count": len(products), # How many actualy returned
        "offset": offset,
        "data": products
    })

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Single product by _id (demonstrates nested queries)."""
    mongo = get_mongo()
    collection = mongo.get_collection("products")
    
    product = collection.find_one({"_id": product_id}, {"_id": 0})
    if not product:
        return jsonify({"status": "error", "message": "Product not found"}), 404
    
    return jsonify({
        "status": "success",
        "data": product
    })
