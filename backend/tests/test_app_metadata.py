from src.api.main import app


def test_app_metadata():
    assert app.title == "Tank Battle Arena Backend"
    assert app.version == "0.1.0"
