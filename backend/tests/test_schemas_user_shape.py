from src.api.schemas import UserBase, UserCreate, UserRead
from datetime import datetime


def test_user_base_and_create_username():
    base = UserBase(username="tester")
    assert base.username == "tester"
    create = UserCreate(username="tester2")
    assert create.username == "tester2"


def test_user_read_fields():
    now = datetime.utcnow()
    read = UserRead(id=1, username="alpha", created_at=now)
    assert read.id == 1
    assert read.username == "alpha"
    assert isinstance(read.created_at, datetime)
