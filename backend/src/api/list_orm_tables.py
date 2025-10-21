from src.api.db import Base
from src.api import models  # noqa: F401  # ensure models are imported to populate metadata


def main():
    # Print discovered ORM tables for quick diagnostics
    tables = sorted(Base.metadata.tables.keys())
    print("\n".join(tables))


if __name__ == "__main__":
    main()
