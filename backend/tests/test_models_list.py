from fastapi.testclient import TestClient

from src.api.main import app


def test_models_list_endpoint():
    client = TestClient(app)
    resp = client.get("/system/models-list")
    assert resp.status_code == 200
    data = resp.json()
    assert "models" in data
    assert isinstance(data["models"], list)
    # Ensure key model names exist
    expected = {"User", "Tank", "Match", "PlayerState", "LeaderboardEntry"}
    assert expected.issubset(set(data["models"]))
