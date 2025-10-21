from fastapi.testclient import TestClient

from src.api.main import app


def test_leaderboard_order_after_seed():
    client = TestClient(app)
    # Seed once
    r = client.post("/system/seed")
    assert r.status_code == 200
    # Fetch leaderboard
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    data = resp.json()
    assert "items" in data
    items = data["items"]
    # Scores should be non-increasing order
    scores = [it["score"] for it in items]
    assert scores == sorted(scores, reverse=True)
