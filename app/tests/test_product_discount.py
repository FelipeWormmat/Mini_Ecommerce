from fastapi.testclient import TestClient

def test_product_discount_create(client: TestClient, admin_auth, payment_method_f, product_factory):
    payment_method = payment_method_f(enabled=True)
    product = product_factory(price=10)

    response = client.post('/product_discount', headers= admin_auth,
    json={
        'mode': 'value',
        'value': 20,
        'payment_method_id': payment_method.id,
        'product_id': product.id,
    })
    print("response",response.json())
    assert response.status_code == 201
    assert response.json()['mode'] == 'value'
    assert response.json()['product_id'] == product.id
    assert response.json()['payment_method_id'] == payment_method.id

def test_product_discount_update(client: TestClient,payment_discount_factory, admin_auth_header):
    payment_discount = payment_discount_factory(mode = 'value')
    response = client.put(f'/product_discount/{payment_discount.id}', headers=admin_auth_header,
                           json={
                                'mode': 'percentage',
                                'value': payment_discount.value,
                                'product_id': payment_discount.product.id,
                                'payment_method_id': payment_discount.payment_method.id
                           })
    print("response",response.json())
    assert response.status_code == 200
    assert response.json()['mode'] == 'percentage'