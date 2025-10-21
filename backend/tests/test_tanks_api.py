from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_create_and_list_tanks():
    # Ensure a user exists to attach the tank to
    ur = client.post("/users", json={"username": "tank_owner"})
    assert ur.status_code in (200, 201), ur.text
    user = ur.json()
    user_id = user["id"]

    # Create a tank
    tr = client.post(
        "/tanks",
        json={
            "user_id": user_id,
            "color": "camo",
            "speed": 1.1,
            "armor": 1.2,
            "damage": 0.9,
        },
    )
    assert tr.status_code in (200, 201), tr.text
    tank = tr.json()
    assert tank["user_id"] == user_id
    assert tank["color"] == "camo"

    # List tanks and verify presence
    lr = client.get("/tanks")
    assert lr.status_code == 200
    tanks = lr.json()
    assert any(t["id"] == tank["id"] for t in tanks)
