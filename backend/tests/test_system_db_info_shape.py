from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_system_db_info_shape():
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "database_url" in data
    # users_count might be None on first run or an integer after table creation
    assert "users_count" in data
    assert (data["users_count"] is None) or isinstance(data["users_count"], int)
