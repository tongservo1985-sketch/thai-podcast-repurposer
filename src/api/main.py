from fastapi import FastAPI, UploadFile, BackgroundTasks
from .models import PodcastJob, JobStatus
import uuid

app = FastAPI(title="OVERLORD API")

@app.post("/upload")
async def upload_podcast(file: UploadFile, user_id: str):
    job_id = str(uuid.uuid4())
    s3_key = f"raw/{user_id}/{job_id}/{file.filename}"
    
    # 1. In real scenario: Upload to S3 here
    # 2. Create DB record
    
    # 3. Dispatch to Celery
    from .tasks import process_transcription_task
    process_transcription_task.delay(job_id, s3_key)
    
    return {"job_id": job_id, "status": "queued"}

@app.get("/job/{job_id}")
async def get_job_status(job_id: str):
    # Fetch status and results from DB
    return {"job_id": job_id, "status": "processing", "progress": "45%"}