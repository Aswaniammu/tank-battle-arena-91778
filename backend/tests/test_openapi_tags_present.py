from fastapi.testclient import TestClient

from src.api.main import app


def test_openapi_tags_present():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()
    assert "tags" in data
    tag_names = {t.get("name") for t in data.get("tags", [])}
    assert "health" in tag_names
    assert "system" in tag_names
