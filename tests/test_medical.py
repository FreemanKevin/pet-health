import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_medical_record():
    response = client.post("/medical/", json={
        "pet_id": 1,
        "visit_date": "2021-01-01",
        "description": "Annual check-up"
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Annual check-up"