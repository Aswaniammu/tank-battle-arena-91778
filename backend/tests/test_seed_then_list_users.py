from fastapi.testclient import TestClient

from src.api.main import app


def test_seed_then_list_users_flow():
    client = TestClient(app)

    # Seed demo data
    r_seed = client.post("/system/seed")
    assert r_seed.status_code == 200
    seed_data = r_seed.json()
    assert seed_data.get("status") == "ok"

    # List users
    r_users = client.get("/users")
    assert r_users.status_code == 200
    users_payload = r_users.json()
    assert "items" in users_payload
    assert "count" in users_payload
    # After seeding we expect at least 2 demo users
    assert users_payload["count"] >= 2
