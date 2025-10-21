from fastapi.testclient import TestClient

from src.api.main import app


def test_leaderboard_payload_fields():
    client = TestClient(app)
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data and "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
    # If any items exist, ensure minimal keys
    if data["items"]:
        e0 = data["items"][0]
        assert "id" in e0
        assert "user_id" in e0
        assert "score" in e0
        assert "updated_at" in e0
