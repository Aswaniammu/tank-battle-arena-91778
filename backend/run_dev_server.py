import os

# PUBLIC_INTERFACE
def main():
    """Run FastAPI app with uvicorn for local development."""
    os.system("uvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001")


if __name__ == "__main__":
    main()
