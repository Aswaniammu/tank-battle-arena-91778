# PUBLIC_INTERFACE
def get_openapi_tags():
    """Return OpenAPI tags used across the backend for consistent documentation."""
    return [
        {"name": "health", "description": "Service health and status"},
        {"name": "system", "description": "System and initialization endpoints"},
        {"name": "docs", "description": "Documentation and usage notes"},
    ]
