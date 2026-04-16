from flask import Blueprint, jsonify, request
from connectors import get_mongo, get_mysql

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    try:
        raw_count = request.args.get('count', '10')
        raw_offset = request.args.get('offset', '0')
        
        limit = int(raw_count)
        offset = int(raw_offset)
        
        if limit < 0: limit = 10
        if offset < 0: offset = 0
    except (ValueError, TypeError):
        limit = 10
        offset = 0

    db = get_mysql()
    with db.get_cursor() as cur:
        query = "SELECT article_number, price FROM product LIMIT %s OFFSET %s"
        cur.execute(query, (limit, offset))
        mysql_data = cur.fetchall()

    if not mysql_data:
        return jsonify({"status": "success", "count": 0, "data": []})

    articles = [row['article_number'] for row in mysql_data]
    mongo = get_mongo()
    mongo_docs = {
        doc["article_number"]: doc.get("clothing_type", "Unknown")
        for doc in mongo.get_collection("products").find(
            {"article_number": {"$in": articles}},
            {"article_number": 1, "clothing_type": 1}
        )
    }

    products = []
    for row in mysql_data:
        art = row['article_number']
        products.append({
            "id": str(art),
            "name": mongo_docs.get(art, "Product " + str(art)),
            "price": float(row['price'])
        })

    return jsonify({
        "status": "success",
        "count": len(products),
    "data": products
    })


@products_bp.route('/<string:article_number>', methods=['GET'])
def get_product_detail(article_number):
    """Single product by _id (demonstrates nested queries)."""
    mysql = get_mysql()
    with mysql.get_cursor() as cur:
        query = "SELECT article_number, product_document_url, price FROM product WHERE article_number = %s"
        cur.execute(query, (article_number,))
        base_info = cur.fetchone()

    if not base_info:
        return jsonify({"status": "error", "message": "Product not found in MySQL"}), 404

    mongo = get_mongo()
    details = mongo.get_collection("products").find_one(
        {"article_number": article_number},
        {"_id": 0}
    )

    full_data = {
        "article": base_info['article_number'],
        "price": float(base_info['price']),
        "image": base_info['product_document_url'],
        "details": details or "No extended description available"
    }

    return jsonify({"status": "success", "data": full_data})

