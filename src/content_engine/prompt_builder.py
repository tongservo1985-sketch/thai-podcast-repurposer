import os
from typing import Dict

class ThaiPromptBuilder:
    """
    Assembles the system and user prompts with the transcription data 
    to ensure nuanced Thai output.
    """
    
    def __init__(self, template_path: str = "prompts/templates/social_platforms.yaml"):
        self.system_core = self._load_core_prompt()
        # In a real app, load from the YAML file
        self.templates = {
            "facebook": "Write a long-form Facebook post summarizing the following transcript in Thai...",
            "threads": "Create a punchy Thread in Thai...",
            "blog": "Write a structured SEO blog post in Thai..."
        }

    def _load_core_prompt(self) -> str:
        # Simplified for example
        return "You are an elite Thai Content Creator..."

    def build_payload(self, transcript: str, platform: str, speaker_context: str = "") -> Dict:
        """
        Generates the messages list for OpenAI/Anthropic API.
        """
        template = self.templates.get(platform, self.templates["facebook"])
        
        user_content = f"""
        TRANSCRIPT:
        {transcript}

        SPEAKER CONTEXT:
        {speaker_context}

        INSTRUCTIONS:
        {template}
        
        Ensure the Thai is natural, uses appropriate particles, and maintains the 'Professional-Casual' tone.
        """

        return {
            "messages": [
                {"role": "system", "content": self.system_core},
                {"role": "user", "content": user_content}
            ],
            "temperature": 0.7, # Balanced creativity
            "top_p": 0.9
        }

# Example Usage:
# builder = ThaiPromptBuilder()
# payload = builder.build_payload("สรุปงานสัมมนาเรื่อง AI...", "facebook", "Host เป็นผู้เชี่ยวชาญด้าน Tech")