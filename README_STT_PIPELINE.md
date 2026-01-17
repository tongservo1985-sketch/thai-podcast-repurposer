# STT Pipeline Documentation (Voice Engineering)

## Overview
This module implements the **Transcription Engine (Worker B)** defined in the `ARCHITECTURE_OVERVIEW.md`. It is optimized for the OVERLORD project's requirement of high-accuracy Thai transcription with seamless English code-switching.

## Key Features
1.  **Audio Normalization:** Uses FFmpeg to ensure consistency (16kHz, mono) regardless of the original podcast recording quality.
2.  **Faster-Whisper Implementation:** Utilizing `large-v3` with CTranslate2 quantization (int8/float16) to achieve near real-time performance on GPU.
3.  **VAD (Voice Activity Detection):** Integrated to ignore long silences, preventing model "hallucinations" common in long-form podcast audio.
4.  **Thai Nuance Handling:** The `ThaiPostProcessor` manages the spacing between Thai script and English technical terms (e.g., "การใช้ AI" vs "การใช้AI").

## Hardware Recommendations
- **Minimum:** 8GB RAM, 4-core CPU (uses `int8` quantization).
- **Recommended:** NVIDIA T4 or better (AWS g4dn.xlarge) for `float16` acceleration.

## Integration with Social Engine
The output JSON contains timestamped segments which are critical for Worker C (Content Transformation) to identify high-energy sections or specific quotes for TikTok/Reels captions.