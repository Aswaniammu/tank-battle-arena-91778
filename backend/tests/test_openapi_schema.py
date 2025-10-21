from fastapi.testclient import TestClient

from src.api.main import app


def test_openapi_schema_generation():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    schema = resp.json()
    assert "openapi" in schema
    assert "paths" in schema
    # Health path should exist
    assert "/" in schema["paths"]
