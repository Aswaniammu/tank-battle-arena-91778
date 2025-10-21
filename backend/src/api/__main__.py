"""
Module entrypoint to run the FastAPI app with Uvicorn.

Usage:
    python -m src.api
"""
import uvicorn

def main():
    """Run the FastAPI application using Uvicorn for local development."""
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=3001, reload=True)

if __name__ == "__main__":
    main()
