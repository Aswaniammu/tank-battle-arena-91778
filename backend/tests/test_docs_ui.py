from fastapi.testclient import TestClient

from src.api.main import app


def test_docs_ui_served():
    client = TestClient(app)
    resp = client.get("/docs")
    assert resp.status_code == 200
    assert "text/html" in resp.headers.get("content-type", "")
