# Scalability & Performance Strategy

## 1. Handling Large Files
- **Multi-part Uploads:** Direct-to-S3 client uploads to bypass API server bottlenecks.
- **VPC Endpoints:** Ensure fast data transfer between S3 and GPU Workers.

## 2. Thai NLP Optimization
- **Whisper Beam Search:** Optimized for Thai to handle "Code-switching" (Thai-English).
- **GPU Inference:** Workers use NVIDIA T4/A100 instances with `Faster-Whisper` for 4x speed improvement.

## 3. Resilience
- **Dead Letter Queues (DLQ):** Failed transcriptions are moved to a separate queue for manual review or retry with a different model.
- **Database Indexing:** Indexing `user_id` and `status` to ensure fast dashboard loading as the user base grows.