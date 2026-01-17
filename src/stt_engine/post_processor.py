import re

class ThaiPostProcessor:
    """
    Cleans and formats Thai transcriptions.
    Handles specific Thai particles and common STT artifacts.
    """
    @staticmethod
    def clean_text(text: str) -> str:
        # Remove repetitive filler words often hallucinated or over-transcribed
        # (e.g., repeating 'ครับ' or 'ค่ะ' in high-latency segments)
        text = re.sub(r'(ครับ|ค่ะ|นะครัับ|นะคะ){2,}', r'\1', text)
        
        # Ensure proper spacing for English words embedded in Thai
        # Thai doesn't use spaces, but English does.
        text = re.re.sub(r'([a-zA-Z])([ก-ฮ])', r'\1 \2', text)
        text = re.re.sub(r'([ก-ฮ])([a-zA-Z])', r'\1 \2', text)
        
        return text.strip()

    @staticmethod
    def format_for_social(segments: list) -> str:
        """
        Helper to prepare a draft for the Transformation Engine.
        """
        return "\n".join([f"[{s['start']}s] {s['text']}" for s in segments])