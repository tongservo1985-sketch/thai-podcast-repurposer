from sqlalchemy import Column, Integer, String, JSON, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
import enum
from .database import Base

class JobStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    TRANSCRIBING = "transcribing"
    TRANSFORMING = "transforming"
    COMPLETED = "completed"
    FAILED = "failed"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_path = Column(String)
    status = Column(Enum(JobStatus), default=JobStatus.PENDING)
    transcription_text = Column(JSON, nullable=True) # Stores Thai segments & timestamps
    social_content = Column(JSON, nullable=True)     # Stores FB, Threads, TikTok output
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, index=True)