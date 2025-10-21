from fastapi.testclient import TestClient

from src.api.main import app


def test_health_structure():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body, dict)
    assert set(body.keys()) == {"message"}
    assert body["message"] == "Healthy"
