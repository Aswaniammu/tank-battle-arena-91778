"""Run the FastAPI backend locally with uvicorn for quick development.

Usage:
  python run_local.py
"""
import uvicorn

# PUBLIC_INTERFACE
def main():
    """Entrypoint to run the FastAPI app with auto-reload for local development."""
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
