import pytest

TEST_SCENARIOS = [
    ("AndreevVA", "Pa$$w0rd", "client", "product", "worker"),
    ("wk_PavlovPP", "Pa$$w0rd", "cashier", "receipt", "supplier"),
    ("wk_IvanovII", "Pa$$w0rd", "worker", "supplier", "mysql.user") 
]

@pytest.mark.parametrize("login, password, expected_role, allowed_table, forbidden_table", TEST_SCENARIOS)
def test_full_user_flow(client, login, password, expected_role, allowed_table, forbidden_table):
    login_res = client.post('/api/login', json={"login": login, "password": password})
    assert login_res.status_code == 200
    
    data = login_res.get_json()['data']
    token = data['token']
    assert data['role'] == expected_role
    
    headers = {'Authorization': f'Bearer {token}'}

    res_ok = client.get(f'/api/data/{allowed_table}', headers=headers)
    assert res_ok.status_code == 200

    res_fail = client.get(f'/api/data/{forbidden_table}', headers=headers)
    assert res_fail.status_code == 403

