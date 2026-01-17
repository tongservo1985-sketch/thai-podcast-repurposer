import os
import shutil
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from .models import Job, JobStatus
from .tasks import process_podcast_pipeline
from .celery_app import celery_app

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="OVERLORD Backend API", version="1.0.0")

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "OVERLORD Thai Podcast AI API is online"}

@app.post("/api/v1/upload")
async def upload_audio(
    file: UploadFile = File(...), 
    user_id: int = 1, # Placeholder for Auth
    db: Session = Depends(get_db)
):
    """
    Handles audio file upload and initiates the AI orchestration pipeline.
    """
    # 1. Save File Locally (or stream to S3)
    file_path = os.path.join(UPLOAD_DIR, f"{user_id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2. Create Job Record
    new_job = Job(
        filename=file.filename,
        file_path=file_path,
        status=JobStatus.PENDING,
        user_id=user_id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    # 3. Trigger Celery Task
    task = process_podcast_pipeline.delay(new_job.id)

    return {
        "job_id": new_job.id,
        "celery_task_id": task.id,
        "status": "Queued",
        "message": "ไฟล์ของคุณกำลังถูกประมวลผล โปรดรอสักครู่"
    }

@app.get("/api/v1/jobs/{job_id}")
async def get_job_status(job_id: int, db: Session = Depends(get_db)):
    """
    Polls the current status of the audio processing job.
    """
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return {
        "id": job.id,
        "status": job.status,
        "created_at": job.created_at,
        "transcription": job.transcription_text if job.status == JobStatus.COMPLETED else None,
        "social_content": job.social_content if job.status == JobStatus.COMPLETED else None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)