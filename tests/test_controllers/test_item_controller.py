from fastapi.testclient import TestClient
from src.burger95s.main import app
from src.services import item_service

client = TestClient(app)

def override_item_service_get_item_by_id(id: int = 0):
    return {
        "id": id,
        "name": "foo",
        "quantity": 1 
    }

app.dependency_overrides[item_service.get_item_by_id] = override_item_service_get_item_by_id

def test_succeed_get_item_by_id():
    response = client.get("/items/{id}/?item_id=0")

    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "id": 0,
        "name": "foo",
        "quantity": 1 
    }

