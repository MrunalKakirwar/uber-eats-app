import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_process_payment(client):
    response = client.post('/api/payment', json={
        "card_number": "1234567812345678",
        "expiry_date": "12/25",
        "cvv": "123",
        "amount": 10.99
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Payment successful"
    assert data["amount_paid"] == 10.99
