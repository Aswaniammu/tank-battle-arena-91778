from fastapi.testclient import TestClient

from src.api.main import app


def test_smoke_list_endpoints():
    client = TestClient(app)
    # Users
    r_users = client.get("/users")
    assert r_users.status_code == 200
    data_users = r_users.json()
    assert isinstance(data_users, dict) and "items" in data_users and "count" in data_users

    # Leaderboard
    r_lb = client.get("/leaderboard")
    assert r_lb.status_code == 200
    data_lb = r_lb.json()
    assert isinstance(data_lb, dict) and "items" in data_lb and "count" in data_lb

    # Models list
    r_models = client.get("/system/models-list")
    assert r_models.status_code == 200
    data_models = r_models.json()
    assert isinstance(data_models, dict) and "models" in data_models
