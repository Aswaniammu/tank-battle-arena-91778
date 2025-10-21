from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_system_diag_shape_and_tables():
    resp = client.get("/system/diag")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "db" in data and isinstance(data["db"], dict)
    assert "database_url" in data["db"]
    assert "tables" in data and isinstance(data["tables"], list)
    # Ensure our core tables are present (created on startup or on first call)
    expected = {"users", "tanks", "matches", "player_states", "leaderboard_entries"}
    assert expected.issubset(set(data["tables"]))
