import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_checkout_order(client):
    response = client.post('/api/order/checkout', json={
        "food_id": 1,
        "food_name": "Burger",
        "price": 5.99
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["total_amount"] == 6.99
    assert data["food_item"] == "Burger"
