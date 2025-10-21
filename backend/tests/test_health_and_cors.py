from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health_ok_and_message():
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Healthy"


def test_cors_headers_present_on_health():
    # Simulate CORS preflight/actual request
    headers = {
        "Origin": "http://example.com",
        "Access-Control-Request-Method": "GET",
    }
    # Preflight
    pre = client.options("/", headers=headers)
    assert pre.status_code in (200, 204)
    # Actual
    res = client.get("/", headers=headers)
    assert res.status_code == 200
    # Check CORS relevant headers added by middleware
    assert "access-control-allow-origin" in (k.lower() for k in res.headers.keys())
