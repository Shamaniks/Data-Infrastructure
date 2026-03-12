import pytest
from app import app
import responses as res

TEST_SCENARIOS = [
    ("AndreevVA", "Pa$$w0rd", "client", "product", "worker"),
    ("wk_PavlovPP", "Pa$$w0rd", "cashier", "receipt", "supplier"),
    ("wk_IvanovII", "Pa$$w0rd", "worker", "supplier", "mysql.user") 
]

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("login, password, expected_role, allowed_table, forbidden_table", TEST_SCENARIOS)
def test_full_user_flow(client, login, password, expected_role, allowed_table, forbidden_table):
    login_res = client.post('/api/login', json={
        "login": login,
        "password": password
    })
    
    assert login_res.status_code == 200, f"Login failed for {login}"
    data = login_res.get_json()
    token = data['data']['token']
    role = data['data']['role']
    
    assert role == expected_role, f"Role mismatch for {login}: expected {expected_role}, got {role}"
    
    headers = {'Authorization': f'Bearer {token}'}

    allowed_res = client.get(f'/api/data/{allowed_table}', headers=headers)
    assert allowed_res.status_code == 200, \
        f"User {login} ({role}) should have access to {allowed_table}, but got {allowed_res.status_code}"

    forbidden_res = client.get(f'/api/data/{forbidden_table}', headers=headers)
    assert forbidden_res.status_code == 403, \
        f"User {login} ({role}) should NOT have access to {forbidden_table}, but got {forbidden_res.status_code}"
