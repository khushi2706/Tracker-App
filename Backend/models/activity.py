from dataclasses import dataclass
from models.conn import Base
from models.enum import ActivityType
from datetime import datetime
from sqlalchemy import (
    String,
    Column,
    Integer,
    Text,
    DateTime,
    BigInteger,
    ForeignKey,
    Enum,
    Boolean,
    Float,
    column,
    event,
)

@dataclass
class Activity(Base):
    __tablename__ = "activity"
    activity_id: int
    user_id: int
    title: str
    distance: float
    activity_type: int
    note: str
    start_at: datetime
    end_at: datetime
    created_at: datetime
    modified_at: datetime

    activity_id = Column("activity_id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", ForeignKey("user.user_id", ondelete="CASCADE"))
    title = Column("title", String(255), nullable=False)
    distance = Column("distance", Float, nullable=False)  
    activity_type = Column("activity_type", Enum(ActivityType), nullable=False)
    note = Column("note", Text)
    start_at = Column("start_at", DateTime, default=datetime.utcnow)
    end_at = Column("end_at", DateTime, default=datetime.utcnow)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)
    modified_at = Column("modified_at", DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Activity activity_id={0}>".format(self.activity_id)