# OVERLORD Backend Services

This is the core API and Task Orchestration layer for the OVERLORD Thai Podcast AI.

## How to Run
1. **Start Redis:** `docker run -p 6379:6379 redis`
2. **Start Postgres:** Ensure a DB is running and updated in `.env`.
3. **Install Dependencies:** `pip install -r requirements.txt`
4. **Run API Service:**