from fastapi.testclient import TestClient
from src.api.main import app


def test_cors_headers_present_on_health():
    client = TestClient(app)
    resp = client.get("/", headers={"Origin": "http://example.com"})
    assert resp.status_code == 200
    # CORS middleware should reflect headers allowing any origin for MVP
    assert resp.headers.get("access-control-allow-origin") in ("*", "http://example.com")
    assert resp.headers.get("access-control-allow-credentials") in (None, "true")
