from datetime import datetime
from src.api.schemas import MatchBase, MatchCreate, MatchRead


def test_match_base_defaults():
    base = MatchBase()
    assert base.status == "ongoing"


def test_match_create_inherits_defaults():
    create = MatchCreate()
    assert create.status == "ongoing"


def test_match_read_fields():
    now = datetime.utcnow()
    read = MatchRead(id=1, started_at=now, ended_at=None, status="ongoing")
    assert read.id == 1
    assert isinstance(read.started_at, datetime)
    assert read.ended_at is None
    assert read.status == "ongoing"
