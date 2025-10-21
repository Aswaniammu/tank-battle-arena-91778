from fastapi.testclient import TestClient

from src.api.main import app


def test_cors_headers_on_root():
    client = TestClient(app)
    # Simulate a browser CORS preflight by including Origin
    resp = client.get("/", headers={"Origin": "http://example.com"})
    assert resp.status_code == 200
    # Since allow_origins=["*"], FastAPI CORS sets wildcard
    assert resp.headers.get("access-control-allow-origin") in ("*", "http://example.com")
    # CORS middleware should expose vary or other headers
    assert "access-control-allow-credentials" in {k.lower(): v for k, v in resp.headers.items()}
