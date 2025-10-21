from fastapi.testclient import TestClient
from src.api.main import app


def test_leaderboard_endpoint_shape():
    client = TestClient(app)
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    # If there are entries, they should have user_id and score
    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        assert "user_id" in entry
        assert "score" in entry
