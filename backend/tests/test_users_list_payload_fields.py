from fastapi.testclient import TestClient

from src.api.main import app


def test_users_list_payload_fields():
    client = TestClient(app)
    resp = client.get("/users")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "items" in data and "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
    # If there is at least one user, ensure expected keys are present
    if data["items"]:
        u0 = data["items"][0]
        assert "id" in u0
        assert "username" in u0
        assert "created_at" in u0
