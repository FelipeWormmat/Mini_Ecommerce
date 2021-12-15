from fastapi.testclient import TestClient

def test_supplier_create(client: TestClient, admin_auth_header):
    response = client.post('/suppliers/', headers=admin_auth_header, json={
        'name': 'Fornecedor 1'
    })
    assert response.status_code == 201
    assert response.json()['id'] == 1

def test_update(client: TestClient, admin_auth_header):
    client = client.post('/suppliers/', headers=admin_auth_header, json={
        'name': 'Fornecedor 1'
    })
    client = client.put('/suppliers/1', headers=admin_auth_header, json={
        'name': 'Fornecedor Atualizado'
    })
    reponse = client.get('/suppliers/1', headers=admin_auth_header)
    assert reponse.status_code == 200


def test_get_all(client: TestClient, admin_auth_header):
    for i in range(1,7):
        client.post('/supplier/',headers=admin_auth_header,json={
            'name' : f'Fornecedor {i}'
        })
    response = client.get('/supplier/', headers=admin_auth_header)
    assert response.status_code == 200
    for i in range(1,7):
        assert response.json()[i-1]['name'] == f'Forncedor {i}'