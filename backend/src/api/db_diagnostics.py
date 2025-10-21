from fastapi import APIRouter
from src.api.db_utils import get_masked_database_url

router = APIRouter(prefix="/system", tags=["system"])


# PUBLIC_INTERFACE
@router.get("/db-url", summary="Database URL (masked)", description="Returns masked database URL and whether default SQLite is used.")
def get_db_url():
    """
    Return diagnostics for database connection string.
    Parameters: none
    Returns: JSON with masked database URL and default flag.
    """
    masked, is_default = get_masked_database_url()
    return {"database_url": masked, "is_default_sqlite": is_default}
