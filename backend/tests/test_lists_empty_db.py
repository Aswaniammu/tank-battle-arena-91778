from fastapi.testclient import TestClient

from src.api.main import app


def test_lists_on_empty_db():
    client = TestClient(app)

    # Ensure endpoints respond even if DB has no data yet
    r_users = client.get("/users")
    assert r_users.status_code == 200
    u = r_users.json()
    assert isinstance(u, dict) and "items" in u and "count" in u
    assert isinstance(u["items"], list)
    assert isinstance(u["count"], int)

    r_lb = client.get("/leaderboard")
    assert r_lb.status_code == 200
    l = r_lb.json()
    assert isinstance(l, dict) and "items" in l and "count" in l
    assert isinstance(l["items"], list)
    assert isinstance(l["count"], int)
