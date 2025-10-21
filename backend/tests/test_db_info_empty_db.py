from fastapi.testclient import TestClient

from src.api.main import app


def test_db_info_empty_db():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    data = resp.json()
    assert "database_url" in data
    # users_count can be None before tables/users are created/populated; allow int or None
    assert "users_count" in data
    assert data["users_count"] is None or isinstance(data["users_count"], int)
