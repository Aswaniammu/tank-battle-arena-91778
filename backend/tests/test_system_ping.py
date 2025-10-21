from fastapi.testclient import TestClient
from src.api.main import app


def test_system_ping_returns_pong():
    client = TestClient(app)
    resp = client.get("/system/ping")
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("ping") == "pong"
