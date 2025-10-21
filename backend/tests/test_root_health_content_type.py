from fastapi.testclient import TestClient

from src.api.main import app


def test_root_health_content_type_and_payload():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.headers.get("content-type", "").startswith("application/json")
    data = resp.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Healthy"
