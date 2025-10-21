import json
import os

# Import app so that all routers and startup wiring are registered prior to schema generation
from src.api.main import app  # noqa: F401

def main() -> None:
    """Generate and write the OpenAPI schema for the backend into interfaces/openapi.json."""
    # PUBLIC_INTERFACE
    openapi_schema = app.openapi()

    output_dir = "interfaces"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "openapi.json")
    with open(output_path, "w") as f:
        json.dump(openapi_schema, f, indent=2)

if __name__ == "__main__":
    main()
