from src.stt_engine.preprocessing import AudioPreprocessor
from src.stt_engine.processor import ThaiSTTEngine
from src.stt_engine.post_processor import ThaiPostProcessor
import json

def run_pipeline(audio_file: str):
    # 1. Preprocessing
    preprocessor = AudioPreprocessor()
    processed_audio = preprocessor.process(audio_file)
    
    # 2. Transcription
    # Use large-v3 for highest accuracy as per Strategic Vision
    stt_engine = ThaiSTTEngine(model_size="large-v3") 
    raw_output = stt_engine.transcribe(processed_audio)
    
    # 3. Post-Processing (Thai-specific cleaning)
    cleaner = ThaiPostProcessor()
    for segment in raw_output['segments']:
        segment['text'] = cleaner.clean_text(segment['text'])
    
    raw_output['full_text'] = cleaner.clean_text(raw_output['full_text'])
    
    # Final Output for the Social Transformation Worker
    print(f"--- Transcription Complete ---")
    print(f"Total Segments: {len(raw_output['segments'])}")
    print(f"Snippet: {raw_output['full_text'][:200]}...")
    
    with open("transcription_output.json", "w", encoding="utf-8") as f:
        json.dump(raw_output, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Example usage:
    # run_pipeline("raw_podcast_episode.mp3")
    pass