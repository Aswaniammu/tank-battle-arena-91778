from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_upsert_and_list_leaderboard():
    # Ensure a user exists
    ur = client.post("/users", json={"username": "leader_user"})
    assert ur.status_code in (200, 201), ur.text
    user = ur.json()
    user_id = user["id"]

    # Upsert leaderboard entry
    lr = client.post("/leaderboard", json={"user_id": user_id, "score": 42})
    assert lr.status_code in (200, 201), lr.text
    entry = lr.json()
    assert entry["user_id"] == user_id
    assert entry["score"] == 42

    # Update leaderboard score
    lr2 = client.post("/leaderboard", json={"user_id": user_id, "score": 99})
    assert lr2.status_code in (200, 201), lr2.text
    entry2 = lr2.json()
    assert entry2["user_id"] == user_id
    assert entry2["score"] == 99

    # List leaderboard
    list_r = client.get("/leaderboard")
    assert list_r.status_code == 200
    items = list_r.json()
    assert any(i["user_id"] == user_id and i["score"] == 99 for i in items)
