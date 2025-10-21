from src.api.db import Base, engine
from src.api.seed import seed_minimal_demo


def main():
    # Ensure tables exist before seeding
    Base.metadata.create_all(bind=engine)
    users_created, match_id = seed_minimal_demo()
    print({"status": "ok", "users_created": users_created, "match_id": match_id})


if __name__ == "__main__":
    main()
