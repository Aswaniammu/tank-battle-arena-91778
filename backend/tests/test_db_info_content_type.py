from fastapi.testclient import TestClient

from src.api.main import app


def test_db_info_content_type_json():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    assert "application/json" in resp.headers.get("content-type", "")
