from fastapi.testclient import TestClient

from src.api.main import app


def test_seed_endpoint_idempotent_and_returns_ids():
    client = TestClient(app)

    # First seed call
    r1 = client.post("/system/seed")
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1.get("status") == "ok"
    assert isinstance(d1.get("users"), int)
    assert isinstance(d1.get("match_id"), int)

    # Second seed call should not fail and should still return structure
    r2 = client.post("/system/seed")
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2.get("status") == "ok"
    assert isinstance(d2.get("users"), int)
    assert isinstance(d2.get("match_id"), int)
