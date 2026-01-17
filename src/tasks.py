import logging
from .celery_app import celery_app
from .database import SessionLocal
from .models import Job, JobStatus
import time

logger = logging.getLogger(__name__)

@celery_app.task(bind=True)
def process_podcast_pipeline(self, job_id: int):
    """
    Orchestrates the AI pipeline: 
    1. Preprocessing -> 2. Thai STT -> 3. Content Transformation
    """
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    
    if not job:
        return "Job not found"

    try:
        # Step 1: Update to Processing
        job.status = JobStatus.PROCESSING
        db.commit()
        logger.info(f"Starting Job {job_id}: {job.filename}")

        # Step 2: Call STT Engine (Whisper)
        # In a real scenario, this calls the Whisper logic previously defined
        job.status = JobStatus.TRANSCRIBING
        db.commit()
        
        # Simulating Thai transcription logic
        # transcription_result = stt_engine.transcribe(job.file_path)
        time.sleep(5) 
        mock_transcription = {
            "full_text": "ยินดีต้อนรับเข้าสู่รายการพอดแคสต์...",
            "segments": [{"start": 0.0, "end": 2.0, "text": "ยินดีต้อนรับ"}]
        }
        job.transcription_text = mock_transcription

        # Step 3: Call Content Transformation (LLM)
        job.status = JobStatus.TRANSFORMING
        db.commit()
        
        # Simulating Prompt Engineering logic
        # social_content = llm_service.generate_thai_content(mock_transcription)
        time.sleep(3)
        mock_social = {
            "facebook_post": "5 เทคนิคปั้นพอดแคสต์ให้ปัง! 🎙️...",
            "tiktok_script": "สรุปสั้นๆ จาก EP นี้ครับ...",
            "threads_hook": "ทำไมคนไทยถึงเลิกทำพอดแคสต์?"
        }
        job.social_content = mock_social

        # Step 4: Finalize
        job.status = JobStatus.COMPLETED
        db.commit()
        logger.info(f"Job {job_id} completed successfully.")

    except Exception as e:
        job.status = JobStatus.FAILED
        db.commit()
        logger.error(f"Job {job_id} failed: {str(e)}")
        raise e
    finally:
        db.close()