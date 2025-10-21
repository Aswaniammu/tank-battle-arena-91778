from fastapi.testclient import TestClient

from src.api.main import app


def test_openapi_has_title_and_version():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()
    info = data.get("info", {})
    assert info.get("title") == "Tank Battle Arena Backend"
    assert info.get("version") == "0.1.0"
