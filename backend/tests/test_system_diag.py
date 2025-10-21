from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_system_ping():
    r = client.get("/system/ping")
    assert r.status_code == 200
    assert r.json() == {"pong": True}


def test_system_echo():
    payload = {"foo": "bar", "n": 42}
    r = client.post("/system/echo", json=payload)
    assert r.status_code == 200
    assert r.json() == {"echo": payload}
