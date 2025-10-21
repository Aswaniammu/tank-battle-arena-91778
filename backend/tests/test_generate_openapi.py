import os
import importlib


def test_generate_openapi_writes_file(tmp_path, monkeypatch):
    # Change CWD to backend so script writes to interfaces/openapi.json under backend/
    backend_dir = os.path.dirname(os.path.dirname(__file__))
    interfaces_dir = os.path.join(backend_dir, "interfaces")
    # Ensure a clean state by removing target file if exists
    target_path = os.path.join(interfaces_dir, "openapi.json")
    if os.path.exists(target_path):
        os.remove(target_path)

    # Import the module to trigger generation
    mod = importlib.import_module("src.api.generate_openapi")
    # After import, the file should exist
    assert os.path.exists(target_path), "OpenAPI file was not created"
