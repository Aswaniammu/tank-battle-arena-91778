import pytest
from fastapi.testclient import TestClient

from src.api.main import app


def test_health_root():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Healthy"
