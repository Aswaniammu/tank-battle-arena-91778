from fastapi.testclient import TestClient

from src.api.main import app


def test_docs_ui_served():
    client = TestClient(app)
    resp = client.get("/docs")
    # Starlette redirects to /docs with HTML; allow 200 or 307 with follow redirects
    if resp.status_code in (301, 302, 303, 307, 308):
        resp = client.get("/docs", follow_redirects=True)
    assert resp.status_code == 200
    assert "text/html" in resp.headers.get("content-type", "")
    assert b"Swagger UI" in resp.content or b"Rapidoc" in resp.content or b"OpenAPI" in resp.content
