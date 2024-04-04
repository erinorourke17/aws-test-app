from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_with_valid_input():
    response = client.get("/test")
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert "message" in data


def test_with_invalid_input():
    response = client.post("/test")
    data = response.json()

    assert response.status_code != status.HTTP_200_OK
    assert "Method Not Allowed" in data["detail"]
