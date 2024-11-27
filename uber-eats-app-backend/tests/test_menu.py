import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_menu(client):
    response = client.get('/api/menu')
    assert response.status_code == 200
    data = response.get_json()
    assert "restaurant" in data
    assert len(data["items"]) == 4
