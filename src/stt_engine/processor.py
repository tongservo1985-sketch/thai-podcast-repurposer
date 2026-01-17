import torch
from faster_whisper import WhisperModel
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class ThaiSTTEngine:
    """
    Core Transcription Engine utilizing Faster-Whisper large-v3.
    Optimized for Thai-English code-switching common in podcasts.
    """
    def __init__(self, model_size: str = "large-v3", device: str = None):
        # Auto-detect CUDA for GPU acceleration
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.compute_type = "float16" if self.device == "cuda" else "int8"
        
        logger.info(f"Initializing Whisper model '{model_size}' on {self.device}")
        self.model = WhisperModel(model_size, device=self.device, compute_type=self.compute_type)

    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        """
        Transcribes Thai audio with timestamps and language detection.
        """
        # language='th' forces Thai context, but Whisper still handles English code-switching
        segments, info = self.model.transcribe(
            audio_path, 
            language="th",
            beam_size=5,
            vad_filter=True, # Remove silences to improve processing speed
            vad_parameters=dict(min_silence_duration_ms=500)
        )

        logger.info(f"Detected language: {info.language} with probability {info.language_probability:.2f}")

        results = []
        full_text = ""

        for segment in segments:
            results.append({
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": segment.text.strip()
            })
            full_text += segment.text + " "

        return {
            "metadata": {
                "detected_language": info.language,
                "language_probability": info.language_probability,
                "duration": info.duration
            },
            "segments": results,
            "full_text": full_text.strip()
        }