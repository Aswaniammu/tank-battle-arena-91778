from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_system_seed_endpoint():
    r = client.post("/system/seed")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    assert data.get("ok") is True
    assert isinstance(data.get("match_id"), int)
