from fastapi.testclient import TestClient

from src.api.main import app


def test_users_list_endpoint():
    client = TestClient(app)
    resp = client.get("/users")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data
    assert "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
