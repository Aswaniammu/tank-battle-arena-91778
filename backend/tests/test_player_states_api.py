from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_create_and_list_player_states():
    # Create a user
    ur = client.post("/users", json={"username": "ps_user"})
    assert ur.status_code in (200, 201), ur.text
    user_id = ur.json()["id"]

    # Create a match
    mr = client.post("/matches")
    assert mr.status_code in (200, 201), mr.text
    match_id = mr.json()["id"]

    # Create a player state
    psr = client.post(
        "/player-states",
        json={
            "match_id": match_id,
            "user_id": user_id,
            "x": 1.0,
            "y": 2.0,
            "angle": 90.0,
            "health": 80.0,
            "score": 5,
        },
    )
    assert psr.status_code in (200, 201), psr.text
    ps = psr.json()
    assert ps["match_id"] == match_id
    assert ps["user_id"] == user_id

    # List player states and ensure presence
    lr = client.get("/player-states")
    assert lr.status_code == 200
    items = lr.json()
    assert any(i["id"] == ps["id"] for i in items)
