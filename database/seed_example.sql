-- Sample Seed Data for Testing Thai NLP Storage
INSERT INTO users (email, password_hash, display_name, plan_type, credits_minutes)
VALUES ('creator@thai-podcast.com', 'argon2_hash_here', 'K. Somchai', 'pro', 120);

INSERT INTO podcasts (user_id, title, description)
VALUES (
    (SELECT id FROM users LIMIT 1),
    'Tech ท้ายซอย',
    'คุยเรื่องเทคโนโลยีแบบบ้านๆ เข้าใจง่าย'
);

INSERT INTO episodes (podcast_id, title, audio_url, status)
VALUES (
    (SELECT id FROM podcasts LIMIT 1),
    'AI จะมาแย่งงานคนไทยจริงไหม?',
    'https://s3.ap-southeast-1.amazonaws.com/overlord/audio/ep1.mp3',
    'completed'
);

INSERT INTO transcriptions (episode_id, full_text, segments)
VALUES (
    (SELECT id FROM episodes LIMIT 1),
    'สวัสดีครับทุกคน วันนี้เราจะมาคุยเรื่อง AI...',
    '[{"start": 0.5, "end": 2.0, "text": "สวัสดีครับทุกคน", "speaker": "A"}]'
);

INSERT INTO social_contents (episode_id, platform, content_text, metadata)
VALUES (
    (SELECT id FROM episodes LIMIT 1),
    'facebook',
    '🚀 AI จะแย่งงานเราจริงหรือ? สรุปประเด็นร้อนจากพอดแคสต์ล่าสุด...',
    '{"hashtags": ["#AI", "#คนไทย", "#Techท้ายซอย"]}'
);