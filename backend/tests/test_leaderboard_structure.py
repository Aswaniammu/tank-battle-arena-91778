from fastapi.testclient import TestClient

from src.api.main import app


def test_leaderboard_structure_and_types():
    client = TestClient(app)
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data and "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
    for item in data["items"]:
        assert "id" in item
        assert "user_id" in item
        assert "score" in item
        assert "updated_at" in item
