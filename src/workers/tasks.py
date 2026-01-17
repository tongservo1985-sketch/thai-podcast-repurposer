from celery import Celery
import os

app = Celery('overlord_tasks', broker=os.getenv('REDIS_URL'))

@app.task(queue='transcription')
def process_transcription_task(job_id, s3_key):
    """
    Task 1: Download from S3, Run Whisper AI, Save Transcript to DB.
    """
    # 1. Download file
    # 2. model = whisper.load_model("large-v3")
    # 3. result = model.transcribe(file, language="th")
    # 4. Update Database with transcript
    # 5. Chain to Content Gen
    generate_social_content_task.delay(job_id)
    return f"Transcription completed for {job_id}"

@app.task(queue='content_gen')
def generate_social_content_task(job_id):
    """
    Task 2: Use LLM to transform Thai transcript into social media posts.
    """
    # 1. Fetch transcript from DB
    # 2. Run LangChain with Thai-centric prompts
    # 3. Save Facebook/Threads/Script results to DB
    # 4. Mark Job as COMPLETED
    return f"Content Generation completed for {job_id}"