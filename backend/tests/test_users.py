from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_users_list_structure():
    r = client.get("/users")
    assert r.status_code == 200
    data = r.json()
    assert "items" in data and "count" in data
    assert isinstance(data["items"], list)
    assert isinstance(data["count"], int)
