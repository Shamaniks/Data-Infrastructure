import pytest
from typing import Dict, Any

import connectors

def test_cart_full_cycle(client: Any):
    """Testing full cycle: login -> add to cart -> check -> delete"""
    
    # 1 Auth
    login_data: Dict[str, str] = {"login": "AndreevVA", "password": "Pa$$w0rd"}
    login_res = client.post('/api/login', json=login_data)
    token: str = login_res.get_json()['data']['token']
    headers: Dict[str, str] = {'Authorization': f'Bearer {token}'}

    # 2 Adding to cartt (Actually we can add unexisted product, but I'm to lazy to fix that)
    product_id: int = 5
    add_res = client.post(f'/api/cart/add/{product_id}?quantity=3', headers=headers)
    assert add_res.status_code == 200
    
    # 3 Checking in redis
    r = connectors.get_redis()
    # Checking hash in redis: key 'cart:AndreevVA', field '5'
    redis_val = r.hget(f"cart:AndreevVA", str(product_id))
    assert redis_val == "3"

    # 4 Getting cart from API
    get_res = client.get('/api/cart/', headers=headers)
    assert get_res.status_code == 200

    response_data = get_res.get_json()['data']
    cart_items = response_data['items'] 
    
    assert str(product_id) in cart_items
    assert int(cart_items[str(product_id)]) == 3
    assert response_data['user_id'] == "AndreevVA"

    # 5 Deleting product
    del_res = client.delete(f'/api/cart/{product_id}', headers=headers)
    assert del_res.status_code == 200
    
    # 6 Checking redis is empty
    assert r.hexists(f"cart:AndreevVA", str(product_id)) is False

