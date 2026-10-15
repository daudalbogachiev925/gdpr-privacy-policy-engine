from fastapi.testclient import TestClient
import pytest

from src.api import app

client = TestClient(app)

def test_api_compliant():
    payload = {
        "data": {
            "user_id": "123",
            "email": "test@example.com",
            "timestamp": "2024-09-01T12:00:00"
        },
        "policy": {
            "name": "simple",
            "required_fields": ["user_id", "email", "timestamp"],
            "prohibited_fields": [],
            "retention_days": 365
        }
    }
    response = client.post("/enforce", json=payload)
    assert response.status_code == 200
    assert response.json()["compliant"] is True

def test_api_non_compliant_missing_field():
    payload = {
        "data": {"email": "test@example.com", "timestamp": "2024-09-01T12:00:00"},
        "policy": {
            "name": "simple",
            "required_fields": ["user_id", "email", "timestamp"],
            "prohibited_fields": [],
            "retention_days": 365
        }
    }
    response = client.post("/enforce", json=payload)
    assert response.status_code == 200
    assert response.json()["compliant"] is False
