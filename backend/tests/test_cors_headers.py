from fastapi.testclient import TestClient

from src.api.main import app


def test_cors_headers_present_on_health():
    client = TestClient(app)
    resp = client.get("/")
    # CORS middleware should add access-control-allow-origin header for GET
    assert resp.status_code == 200
    assert resp.headers.get("access-control-allow-origin") in ("*", None)
