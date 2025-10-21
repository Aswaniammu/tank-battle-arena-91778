from fastapi.testclient import TestClient

from src.api.main import app


def test_db_info_endpoint():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    payload = resp.json()
    assert "database_url" in payload
    # users_count may be None if first run or 0 if empty
    assert "users_count" in payload
