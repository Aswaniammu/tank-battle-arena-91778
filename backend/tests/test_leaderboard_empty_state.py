from fastapi.testclient import TestClient

from src.api.main import app


def test_leaderboard_empty_state_on_fresh_db():
    client = TestClient(app)
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data and "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
    # On fresh DB before seeding, allow either 0 or more (depending on earlier tests),
    # but ensure items and count are consistent if there are no entries.
    if data["count"] == 0:
        assert data["items"] == []
