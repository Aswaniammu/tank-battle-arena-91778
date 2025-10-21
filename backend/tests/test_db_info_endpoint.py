from fastapi.testclient import TestClient

from src.api.main import app


def test_db_info_endpoint_masking_and_count():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    data = resp.json()
    assert "database_url" in data
    assert "users_count" in data
    # For SQLite default, ensure masking to default path
    assert data["database_url"].startswith("sqlite:///")
