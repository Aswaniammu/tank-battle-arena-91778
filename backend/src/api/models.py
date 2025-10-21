"""SQLAlchemy ORM models for the Tank Battle Arena MVP.

Tables:
- users: players with unique usernames
- tanks: customizable tanks belonging to users
- matches: game sessions
- player_states: per-match state for each user
- leaderboard_entries: per-user cumulative scores

Relationships and indexes are defined for efficient querying.
"""
from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
    Float,
    Index,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.api.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    # relationships
    tanks: Mapped[List["Tank"]] = relationship("Tank", back_populates="user", cascade="all, delete-orphan")
    matches: Mapped[List["PlayerState"]] = relationship(
        "PlayerState", back_populates="user", cascade="all, delete-orphan"
    )
    leaderboard_entries: Mapped[List["LeaderboardEntry"]] = relationship(
        "LeaderboardEntry", back_populates="user", cascade="all, delete-orphan"
    )


class Tank(Base):
    __tablename__ = "tanks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    color: Mapped[str] = mapped_column(String(16), nullable=False, default="green")
    speed: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    armor: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    damage: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)

    user: Mapped[User] = relationship("User", back_populates="tanks")

    __table_args__ = (
        Index("ix_tanks_user_id", "user_id"),
    )


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="ongoing")  # ongoing|completed|abandoned

    players: Mapped[List["PlayerState"]] = relationship(
        "PlayerState", back_populates="match", cascade="all, delete-orphan"
    )


class PlayerState(Base):
    __tablename__ = "player_states"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    x: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    y: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    angle: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    health: Mapped[float] = mapped_column(Float, nullable=False, default=100.0)
    score: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    match: Mapped[Match] = relationship("Match", back_populates="players")
    user: Mapped[User] = relationship("User", back_populates="matches")

    __table_args__ = (
        Index("ix_player_states_match_user", "match_id", "user_id", unique=True),
        Index("ix_player_states_user_id", "user_id"),
    )


class LeaderboardEntry(Base):
    __tablename__ = "leaderboard_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    score: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user: Mapped[User] = relationship("User", back_populates="leaderboard_entries")

    __table_args__ = (
        Index("ix_leaderboard_user_id", "user_id", unique=True),
        Index("ix_leaderboard_score_desc", "score"),
    )
