from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

"""
Pydantic schemas for API input/output.

- Uses from_attributes=True for ORM model compatibility (Pydantic v2).
"""


# User Schemas
class UserBase(BaseModel):
    username: str = Field(..., description="Unique username for the player")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Tank Schemas
class TankBase(BaseModel):
    color: str = Field("green", description="Color/style of the tank")
    speed: float = Field(1.0, description="Movement speed multiplier")
    armor: float = Field(1.0, description="Armor multiplier")
    damage: float = Field(1.0, description="Damage multiplier")


class TankCreate(TankBase):
    user_id: int


class TankRead(TankBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


# Match Schemas
class MatchBase(BaseModel):
    status: str = Field("ongoing", description="Match status")


class MatchCreate(MatchBase):
    pass


class MatchRead(MatchBase):
    id: int
    started_at: datetime
    ended_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# PlayerState Schemas
class PlayerStateBase(BaseModel):
    x: float = Field(0.0, description="X coordinate in arena")
    y: float = Field(0.0, description="Y coordinate in arena")
    angle: float = Field(0.0, description="Facing angle in degrees")
    health: float = Field(100.0, description="Player health")
    score: int = Field(0, description="Player score")


class PlayerStateCreate(PlayerStateBase):
    match_id: int
    user_id: int


class PlayerStateRead(PlayerStateBase):
    id: int
    match_id: int
    user_id: int

    class Config:
        from_attributes = True


# Leaderboard Schemas
class LeaderboardEntryBase(BaseModel):
    score: int = Field(0, description="Cumulative score for the leaderboard")


class LeaderboardEntryCreate(LeaderboardEntryBase):
    user_id: int


class LeaderboardEntryRead(LeaderboardEntryBase):
    id: int
    user_id: int
    updated_at: datetime

    class Config:
        from_attributes = True
