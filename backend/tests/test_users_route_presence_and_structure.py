from fastapi.testclient import TestClient

from src.api.main import app


def test_users_route_presence_and_structure():
    client = TestClient(app)
    resp = client.get("/users")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data and isinstance(data["items"], list)
    assert "count" in data and isinstance(data["count"], int)
