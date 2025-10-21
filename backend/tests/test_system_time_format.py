from fastapi.testclient import TestClient

from src.api.main import app


def test_system_time_format():
    client = TestClient(app)
    resp = client.get("/system/time")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "now" in data
    # ISO-like string ending with Z
    assert isinstance(data["now"], str)
    assert data["now"].endswith("Z")
    # Minimal sanity check: contains 'T' separator
    assert "T" in data["now"]
