from dataclasses import dataclass
from models.conn import Base
from datetime import datetime
from sqlalchemy import (
    String,
    Column,
    Integer,
    DateTime,
)

@dataclass
class User(Base):
    __tablename__ = "user"
    user_id: int
    username: str
    password: str
    fname: str
    created_at: datetime
    modified_at: datetime

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(255), nullable=False, unique=True)
    password = Column("password", String(100), nullable=False)  
    fname = Column("fname", String(255))
    created_at = Column("created_at", DateTime, default=datetime.utcnow)
    modified_at = Column("modified_at", DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<User user_id={0} username={1}>".format(self.user_id, self.username)