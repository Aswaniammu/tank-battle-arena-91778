import types

def test_generate_openapi_executes(monkeypatch):
    # Importing should execute without raising and produce an openapi dict
    from src.api import generate_openapi  # noqa: F401
    from src.api.main import app

    schema = app.openapi()
    assert isinstance(schema, dict)
    # basic paths presence
    assert "/" in schema.get("paths", {})
    # system routes should be present
    sys_paths = schema.get("paths", {})
    assert any(p.startswith("/system/") for p in sys_paths.keys())
