from fastapi.testclient import TestClient
from src.api.main import app


def test_system_db_info_structure():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "database_url" in data
    assert "users_count" in data
    # database_url should be a string
    assert isinstance(data["database_url"], str)
    # users_count can be int or None if table not yet populated
    assert data["users_count"] is None or isinstance(data["users_count"], int)
