def test_routes_module_importable():
    import importlib
    m = importlib.import_module("src.api.routes")
    assert hasattr(m, "router")
