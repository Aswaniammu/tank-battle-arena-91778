from fastapi.testclient import TestClient

from src.api.main import app


def test_seed_idempotent_keys():
    client = TestClient(app)
    for _ in range(3):
        resp = client.post("/system/seed")
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, dict)
        assert "status" in data and data["status"] == "ok"
        assert "users_created" in data
        assert "match_id" in data
