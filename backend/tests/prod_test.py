import pytest
from connectors import get_mongo, get_mysql

def test_get_products_default_count(client, mongo_collection):
    """Default ?count=10 returns exactly 5 products"""
    mongo_collection.insert_many([
        {"_id": i, "clothing_type": f"Product {i}", "price": 100 + i} for i in range(1, 6)
    ])
    
    response = client.get("/api/products/")
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["status"] == "success"
    assert data["count"] == 5
    assert len(data["data"]) == 5
    
    # Only required fields
    for item in data["data"]:
        assert set(item.keys()) == {"id", "name", "price"}
        assert isinstance(item["id"], str)
        assert isinstance(item["name"], str)
        assert isinstance(item["price"], (int, float))

def test_get_products_custom_count(client, mongo_collection):
    """?count=3 returns exactly 3 products."""
    mongo_collection.insert_many([
        {"_id": i, "clothing_type": f"Product {i}", "price": 100 + i} for i in range(1, 6)
    ])
    
    response = client.get("/api/products/?count=3")
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["count"] == 3
    assert len(data["data"]) == 3

def test_get_products_count_validation(client, mongo_collection):
    """Invalid count falls back to default 10"""
    mongo_collection.insert_many([
        {"_id": i, "clothing_type": f"Product {i}", "price": 100 + i} for i in range(1, 6)
    ])
    
    response = client.get("/api/products/?count=abc")  # invalid
    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 5

def test_get_products_negative_count(client, mongo_collection):
    """Negative count is treated as default 10."""
    mongo_collection.insert_many([
        {"_id": i, "clothing_type": f"Product {i}", "price": 100 + i} for i in range(1, 6)
    ])
    
    response = client.get("/api/products/?count=-5")
    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 5

def test_get_products_empty_collection(client, mongo_collection):
    """No products count=0, empty list."""
    db = get_mysql()
    with db.get_cursor(db_user=db.root_user, db_pass=db.root_password) as cur:
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        cur.execute("TRUNCATE TABLE product")
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    response = client.get("/api/products/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 0
    assert data["data"] == []
