from fastapi.testclient import TestClient
from src.api.main import app


def test_openapi_contains_expected_tags_and_summaries():
    client = TestClient(app)
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    data = resp.json()

    # Check tags exist
    tags = data.get("tags", [])
    tag_names = {t.get("name") for t in tags}
    assert "health" in tag_names
    assert "system" in tag_names

    # Check specific paths summaries exist
    paths = data.get("paths", {})
    # Health endpoint summary
    if "/" in paths and "get" in paths["/"]:
        assert "summary" in paths["/"]["get"]
        assert paths["/"]["get"]["summary"] == "Health Check"

    # db-info endpoint summary
    if "/system/db-info" in paths and "get" in paths["/system/db-info"]:
        assert "summary" in paths["/system/db-info"]["get"]
        assert paths["/system/db-info"]["get"]["summary"] == "Database Info"
