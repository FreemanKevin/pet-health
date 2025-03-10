import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_pet():
    response = client.post("/pets/", json={
        "name": "Buddy",
        "species": "Dog",
        "breed": "Golden Retriever",
        "birth_date": "2020-01-01",
        "owner_name": "John Doe",
        "chip_number": "123456789"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy"