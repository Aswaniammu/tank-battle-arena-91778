from fastapi.testclient import TestClient

from src.api.main import app


def test_db_url_masking():
    client = TestClient(app)
    resp = client.get("/system/db-info")
    assert resp.status_code == 200
    payload = resp.json()
    assert "database_url" in payload
    # For SQLite default, it should show sqlite:///./data/app.db
    db_url = payload["database_url"]
    assert isinstance(db_url, str)
    assert db_url.startswith("sqlite:///")
