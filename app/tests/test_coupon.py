from fastapi.testclient import TestClient

def test_create(client: TestClient, admin_auth_header):
    response = client.post('/coupons/', headers=admin_auth_header, json={
        'code':'test',
        'expire_at':'2022-12-15T25:14',
        'limit':None,
        'type':'value',
        'value':None
    })
    assert response.status_code == 201
    response = client.get('/coupons/1', headers=admin_auth_header)
    assert response.status_code == 200
    assert response.json()['code'] == 'test'
    assert response.json()['expire_at'] == '2022-12-15T12:25:14'
    assert response.json()['limit'] == None
    assert response.json()['type'] == 'value'
    assert response.json()['value'] == None

def test_update(client:TestClient, admin_auth_header):
    client.post('/coupons/', headers=admin_auth_header, json={
        'code':'test',
        'expire_at':'2022-12-12T15:25:14',
        'limit':None,
        'type':'value',
        'value':None
    })
    assert client.put('/coupons/1', headers=admin_auth_header, json={
        'limit':5,
        'expire_at': '2055-12-15T12:25:14'
    }).status_code == 200