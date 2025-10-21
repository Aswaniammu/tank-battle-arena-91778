from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_system_version():
    r = client.get("/system/version")
    assert r.status_code == 200
    data = r.json()
    assert "version" in data
    assert isinstance(data["version"], str)
    assert data["version"].count(".") >= 1
