from fastapi.testclient import TestClient
from src.api.main import app


def test_health_endpoint_returns_message():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Healthy"
