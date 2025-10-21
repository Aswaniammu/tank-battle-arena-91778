from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_system_help_shape():
    resp = client.get("/system/help")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "title" in data
    assert "description" in data
    assert "websocket_notes" in data
    assert "endpoints" in data and isinstance(data["endpoints"], dict)
    # Ensure some expected endpoints are listed
    eps = data["endpoints"]
    assert "GET /" in eps
    assert "GET /system/time" in eps
    assert "POST /system/seed" in eps
    assert "GET /system/db-info" in eps
