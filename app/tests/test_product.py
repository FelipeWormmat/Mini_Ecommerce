from fastapi.testclient import TestClient

def test_product_create(client: TestClient, admin_auth, category_factory, supplier_factory):
    category = category_factory
    supplier = supplier_factory()

    response = client.post('/product/', headers=admin_auth,
                           json={
                               'description': 'texto',
                               'price': 10,
                               'image': 'rotas de imagens',
                               'technical_details': 'qualquer coisa',
                               'visible': True,
                               'category_id': category.id,
                               'supplier_id': supplier.id
                           })

    assert response.status_code == 201
    assert response.json()['description'] == 'text'
    assert response.json()['category_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id