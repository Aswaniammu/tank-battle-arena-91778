from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_system_time_endpoint_shape():
    resp = client.get("/system/time")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "iso" in data and isinstance(data["iso"], str)
    assert "epoch" in data and isinstance(data["epoch"], int)
