"""
Seed runner utility.

Usage:
  python -m src.api.seed_run
"""
from src.api.main import app  # noqa: F401  # ensures startup side-effects (metadata import) are available
from src.api.db import Base, engine
from src.api.seed import seed_minimal_demo


def main():
    # Ensure tables exist before seeding
    Base.metadata.create_all(bind=engine)
    users_created, match_id = seed_minimal_demo()
    print(f"Seed complete: users_created={users_created}, match_id={match_id}")


if __name__ == "__main__":
    main()
