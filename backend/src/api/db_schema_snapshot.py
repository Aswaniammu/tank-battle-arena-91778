from sqlalchemy import inspect
from src.api.db import engine, Base  # ensure engine is initialized
from src.api import models  # noqa: F401 - import models to register metadata
import json


# PUBLIC_INTERFACE
def snapshot_schema(output_path: str = "interfaces/db_schema_snapshot.json") -> str:
    """Dump current DB tables and columns to a JSON file and return the path."""
    insp = inspect(engine)
    data = {}
    for table in sorted(insp.get_table_names()):
        cols = []
        for col in insp.get_columns(table):
            cols.append({
                "name": col.get("name"),
                "type": str(col.get("type")),
                "nullable": col.get("nullable"),
                "default": str(col.get("default")) if col.get("default") is not None else None,
                "primary_key": col.get("primary_key", False),
            })
        data[table] = cols
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    return output_path


if __name__ == "__main__":
    path = snapshot_schema()
    print(f"Schema snapshot written to {path}")
