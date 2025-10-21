def test_generate_openapi_module_import():
    # Importing the module should execute without raising; it will generate the schema in interfaces/
    import importlib

    m = importlib.import_module("src.api.generate_openapi")
    assert hasattr(m, "openapi_schema")
    assert isinstance(m.openapi_schema, dict)
