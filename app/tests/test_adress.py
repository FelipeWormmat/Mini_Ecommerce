from fastapi.testclient import TestClient
from sqlalchemy.sql.elements import Null

def test_adress_create(client: TestClient):
    response = client.post('/adresses/1', json={
        'name': 'Rua Tal'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1

def test_adress_update(client: TestClient):
    response = client.post('/adresses/1', json={
        'name': 'Rua tal'
    })
    assert response.status_code == 201

    response = client.put(
        '/adresses/1', json={'name': 'Rua Alterada'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Rua alterada'