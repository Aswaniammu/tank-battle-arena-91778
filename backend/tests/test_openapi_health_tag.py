from fastapi.testclient import TestClient
from src.api.main import app


def test_openapi_root_has_health_tag():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()
    paths = data.get("paths", {})
    assert "/" in paths
    get_item = paths["/"].get("get", {})
    tags = get_item.get("tags", [])
    assert "health" in tags
