import ffmpeg
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AudioPreprocessor:
    """
    Handles audio normalization and conversion to the format 
    optimal for Whisper models (16kHz, mono, 16-bit PCM).
    """
    def __init__(self, output_dir: str = "temp/processed"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def process(self, input_path: str) -> str:
        filename = os.path.basename(input_path).rsplit('.', 1)[0]
        output_path = os.path.join(self.output_dir, f"{filename}_normalized.wav")
        
        try:
            logger.info(f"Normalizing audio: {input_path}")
            (
                ffmpeg
                .input(input_path)
                .output(output_path, ar='16000', ac='1', acodec='pcm_s16le')
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            return output_path
        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode()}")
            raise RuntimeError("Failed to process audio file.")