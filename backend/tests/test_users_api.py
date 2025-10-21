from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_create_and_list_users():
    # create a user
    r = client.post("/users", json={"username": "tester1"})
    assert r.status_code in (200, 201), r.text
    data = r.json()
    assert data["username"] == "tester1"
    assert isinstance(data["id"], int)

    # list users and ensure the user is present
    r2 = client.get("/users")
    assert r2.status_code == 200
    users = r2.json()
    assert any(u["username"] == "tester1" for u in users)
