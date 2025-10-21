import json
import os

# PUBLIC_INTERFACE
def main():
    """Generate and write the OpenAPI schema to backend/interfaces/openapi.json."""
    from src.api.main import app  # lazy import to ensure all routers are registered

    schema = app.openapi()
    output_dir = "interfaces"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "openapi.json")
    with open(output_path, "w") as f:
        json.dump(schema, f, indent=2)
    print(f"OpenAPI schema written to {output_path}")


if __name__ == "__main__":
    main()
