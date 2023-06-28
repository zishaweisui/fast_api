from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime 

from database import Base

class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    content = Column(String, nullable=False)
    created_date = Column(
        DateTime, default=datetime.utcnow
    )
    updated_date = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    lname = Column(String(32), unique=False)
    fname = Column(String(32))
    created_date = Column(
        DateTime, default=datetime.utcnow
    )
    updated_date = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = relationship(
        Note,
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.updated_date)"
    )   
