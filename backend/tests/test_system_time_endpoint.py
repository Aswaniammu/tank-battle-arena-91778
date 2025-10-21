from fastapi.testclient import TestClient
from src.api.main import app


def test_system_time_returns_iso_string():
    client = TestClient(app)
    resp = client.get("/system/time")
    assert resp.status_code == 200
    data = resp.json()
    assert "now" in data
    assert isinstance(data["now"], str)
    # Basic sanity: ISO-ish format containing 'T'
    assert "T" in data["now"]
