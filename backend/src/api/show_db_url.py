"""
Small helper to print the resolved database URL used by the backend.

Usage:
    python -m src.api.show_db_url
"""
from src.api.db import DATABASE_URL

def main():
    # PUBLIC_INTERFACE
    def get_db_url() -> str:
        """Return the resolved database URL (masked for default SQLite path)."""
        # For consistency with the /system/db-info route
        if DATABASE_URL.startswith("sqlite"):
            return "sqlite:///./data/app.db"
        return DATABASE_URL

    print(get_db_url())

if __name__ == "__main__":
    main()
