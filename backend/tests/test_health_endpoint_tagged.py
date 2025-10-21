from fastapi.testclient import TestClient

from src.api.main import app


def test_health_endpoint_is_tagged_health():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()
    paths = data.get("paths", {})
    root = paths.get("/", {})
    get_op = root.get("get", {})
    tags = get_op.get("tags", [])
    assert "health" in tags
