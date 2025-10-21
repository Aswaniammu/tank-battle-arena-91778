import os
import json
from importlib import import_module

def test_generate_openapi_main_runs_and_writes_file(tmp_path, monkeypatch):
    # Change CWD to backend so interfaces/ writes in the correct place under temp
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
    mod = import_module("src.api.generate_openapi")
    # Remove existing output if present
    out_dir = "interfaces"
    out_file = os.path.join(out_dir, "openapi.json")
    if os.path.exists(out_file):
        os.remove(out_file)
    # Run main
    mod.main()
    # Verify file exists and is valid JSON
    assert os.path.exists(out_file)
    with open(out_file, "r") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "openapi" in data
    assert "paths" in data
