from fastapi.testclient import TestClient
from sqlalchemy.sql.elements import Null

def test_supplier_create(client: TestClient):
    response = client.post('/supplier', json={
        'name': None
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1

def test_supplier_update(client: TestClient):
    response = client.post('/supplier/', json={
        'name': 'Supplier'
    })
    assert response.status_code == 201

    response = client.put(
        '/supplier/1', json={'name': 'Update Supplier'})

    assert response.status_code == 200
    assert response.json()['name'] == 'OK'
