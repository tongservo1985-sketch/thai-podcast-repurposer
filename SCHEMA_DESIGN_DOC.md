# Database Design Document: OVERLORD Thai Podcast AI

## 1. Design Philosophy
The schema is designed for a **Multi-tenant SaaS** model. It prioritizes data integrity for audio processing states and flexibility for multi-platform content generation. Given the nature of Thai language processing, we use `UTF-8` (specifically `utf8mb4` in MySQL or standard UTF-8 in PostgreSQL) to ensure all Thai characters and emojis are stored correctly.

## 2. Key Entities
- **Users & Subscriptions:** Manages access and "Credits" (minutes of audio processing).
- **Podcasts & Episodes:** The core hierarchy. Episodes act as the parent for all AI-generated artifacts.
- **Transcriptions:** Stores the raw output and timestamped segments (JSONB) for the "Thai-Centric NLP" engine.
- **Social Content:** Stores platform-specific transformations (Facebook, Threads, TikTok, etc.).
- **Jobs:** An audit trail for the asynchronous processing pipeline.

## 3. Data Types & Constraints
- **UUIDs:** Used for primary keys to prevent ID enumeration and facilitate distributed scaling.
- **JSONB (PostgreSQL):** Used for storing dynamic AI metadata, such as confidence scores per word or platform-specific metadata (hashtags, suggested emojis).
- **Status Enums:** To track the lifecycle of audio processing (Queued -> Processing -> Completed -> Failed).