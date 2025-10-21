# OpenAPI generation

Use the helper script to regenerate the OpenAPI schema after updating routes or models:

python -m src.api.generate_openapi

This writes interfaces/openapi.json at the backend root. Ensure the FastAPI app imports all routes before generating so endpoints appear in the spec.
