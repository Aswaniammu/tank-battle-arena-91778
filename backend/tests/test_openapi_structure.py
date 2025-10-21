from fastapi.testclient import TestClient

from src.api.main import app


def test_openapi_structure_basic():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()
    assert "openapi" in data
    assert "info" in data and isinstance(data["info"], dict)
    assert "paths" in data and isinstance(data["paths"], dict)
