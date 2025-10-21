from fastapi.testclient import TestClient

from src.api.main import app


def test_seed_idempotency_and_shape():
    client = TestClient(app)

    # First seed
    r1 = client.post("/system/seed")
    assert r1.status_code == 200
    data1 = r1.json()
    assert data1.get("status") == "ok"
    assert "users_created" in data1
    assert "match_id" in data1

    # Second seed should not error and still return ok
    r2 = client.post("/system/seed")
    assert r2.status_code == 200
    data2 = r2.json()
    assert data2.get("status") == "ok"
    assert "users_created" in data2
    assert "match_id" in data2
