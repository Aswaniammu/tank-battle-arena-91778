from src.api.main import app


def test_openapi_includes_system_and_health():
    schema = app.openapi()
    assert "tags" in schema
    # Ensure our documented tags exist
    tag_names = {t.get("name") for t in schema.get("tags", [])}
    assert "health" in tag_names
    assert "system" in tag_names

    # Ensure paths include our expected endpoints
    paths = schema.get("paths", {})
    assert "/" in paths
    assert "/system/db-info" in paths
    assert "/system/time" in paths
    assert "/system/seed" in paths
    assert "/system/help" in paths
