from src.api.main import app

# Ensure our newly added endpoints are registered
def test_system_endpoints_present():
    paths = app.openapi()["paths"]
    assert "/system/db-info" in paths
    assert "/system/time" in paths
    assert "/system/seed" in paths
    assert "/system/help" in paths
