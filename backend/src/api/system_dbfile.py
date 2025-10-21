"""System endpoints related to database file inspection."""
import os
from pathlib import Path
from fastapi import APIRouter
from src.api.db import DATABASE_URL

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get(
    "/db-file",
    summary="Database file info",
    description="Reports SQLite database file path (masked), existence, and size in bytes when using sqlite.",
    operation_id="system_db_file_info",
)
def db_file_info():
    """Return info about the SQLite DB file if using sqlite; otherwise return the DATABASE_URL type."""
    is_sqlite = DATABASE_URL.startswith("sqlite")
    info = {"database_url": "sqlite:///./data/app.db" if is_sqlite else DATABASE_URL, "is_sqlite": is_sqlite}
    if is_sqlite:
        # Extract file path from URL: sqlite:////abs or sqlite:///rel
        prefix = "sqlite:///"
        path = DATABASE_URL[len(prefix):]
        file_path = Path(path)
        exists = file_path.exists()
        size = file_path.stat().st_size if exists else 0
        # Try write check by touching a temp file in the same folder
        writable = False
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            testfile = file_path.parent / ".write_test"
            with open(testfile, "w") as f:
                f.write("ok")
            testfile.unlink(missing_ok=True)
            writable = True
        except Exception:
            writable = False
        info.update({"file_path": str(file_path), "exists": exists, "size_bytes": size, "writable": writable})
    return info
