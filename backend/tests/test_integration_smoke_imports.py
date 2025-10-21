def test_integration_smoke_imports():
    import importlib

    modules = [
        "src.api.main",
        "src.api.db",
        "src.api.models",
        "src.api.schemas",
        "src.api.seed",
    ]
    for m in modules:
        mod = importlib.import_module(m)
        assert mod is not None
