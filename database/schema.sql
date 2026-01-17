-- OVERLORD: Thai Podcast AI Assistant Schema
-- Target: PostgreSQL 15+

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Custom Types for State Management
CREATE TYPE processing_status AS ENUM ('queued', 'processing', 'completed', 'failed');
CREATE TYPE content_platform AS ENUM ('facebook', 'threads', 'tiktok', 'instagram', 'blog_seo', 'youtube_description');
CREATE TYPE subscription_plan AS ENUM ('free', 'pro', 'enterprise');

-- 1. Users & Profiles
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    display_name VARCHAR(100),
    plan_type subscription_plan DEFAULT 'free',
    credits_minutes INT DEFAULT 30, -- Remaining minutes for processing
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Podcasts (The "Show" container)
CREATE TABLE podcasts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    cover_image_url TEXT,
    language VARCHAR(10) DEFAULT 'th-TH',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Episodes (The Audio Source)
CREATE TABLE episodes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    podcast_id UUID REFERENCES podcasts(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    audio_url TEXT NOT NULL,
    duration_seconds INT,
    file_size_bytes BIGINT,
    status processing_status DEFAULT 'queued',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE
);

-- 4. Transcriptions (Result of Worker B)
CREATE TABLE transcriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    episode_id UUID UNIQUE REFERENCES episodes(id) ON DELETE CASCADE,
    full_text TEXT, -- Raw Thai text
    segments JSONB, -- Array of {start, end, speaker, text}
    confidence_score DECIMAL(3, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Social Content (Result of Worker C)
CREATE TABLE social_contents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    episode_id UUID REFERENCES episodes(id) ON DELETE CASCADE,
    platform content_platform NOT NULL,
    content_text TEXT NOT NULL, -- The generated Thai copy
    metadata JSONB, -- Contains {suggested_hashtags: [], tone: "formal"}
    is_edited_by_user BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Processing Jobs (Audit Trail for Celery)
CREATE TABLE processing_jobs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    episode_id UUID REFERENCES episodes(id) ON DELETE CASCADE,
    job_type VARCHAR(50), -- 'transcription', 'summarization', 'social_gen'
    status processing_status DEFAULT 'queued',
    error_log TEXT,
    worker_node_id VARCHAR(100),
    started_at TIMESTAMP WITH TIME ZONE,
    finished_at TIMESTAMP WITH TIME ZONE
);

-- Indexes for performance
CREATE INDEX idx_episodes_status ON episodes(status);
CREATE INDEX idx_social_contents_platform ON social_contents(platform);
CREATE INDEX idx_podcasts_user_id ON podcasts(user_id);

-- Update trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_modtime BEFORE UPDATE ON users FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_social_modtime BEFORE UPDATE ON social_contents FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();