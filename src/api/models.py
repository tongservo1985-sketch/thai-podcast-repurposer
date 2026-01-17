from sqlalchemy import Column, Integer, String, JSON, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()

class JobStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    TRANScribing = "transcribing"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"

class PodcastJob(Base):
    __tablename__ = "podcast_jobs"

    id = Column(String, primary_key=True)
    user_id = Column(String, index=True)
    original_filename = Column(String)
    s3_key = Column(String)
    status = Column(Enum(JobStatus), default=JobStatus.PENDING)
    transcript = Column(JSON, nullable=True) # Stores timestamps and text
    social_content = Column(JSON, nullable=True) # Stores FB, IG, TikTok drafts
    created_at = Column(DateTime, default=datetime.datetime.utcnow)