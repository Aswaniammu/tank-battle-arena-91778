from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_create_and_list_matches():
    # Create a match
    r = client.post("/matches")
    assert r.status_code in (200, 201), r.text
    match = r.json()
    assert isinstance(match["id"], int)
    assert match["status"] == "ongoing"

    # List matches and ensure the created one is present
    r2 = client.get("/matches")
    assert r2.status_code == 200
    matches = r2.json()
    assert any(m["id"] == match["id"] for m in matches)
