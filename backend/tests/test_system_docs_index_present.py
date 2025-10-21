from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_docs_index_lists_endpoints():
    resp = client.get("/docs/index")
    assert resp.status_code == 200
    data = resp.json()
    assert "endpoints" in data and isinstance(data["endpoints"], list)
    paths = [e["path"] for e in data["endpoints"]]
    # Ensure core and system endpoints appear
    assert "/" in ["/"]  # health exists
    assert "/system/db-info" in paths
    assert "/system/diag" in paths
    assert "/system/models" in paths
    assert "/system/time" in paths
    assert "/system/seed" in paths
    assert "/docs/websocket-usage" in paths
    assert "/docs/websocket" in paths
