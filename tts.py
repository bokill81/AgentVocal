import os
import requests
from dotenv import load_dotenv
import uuid

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "")
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"

def generate_speech(text: str) -> str:
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    voice = VOICE_ID or "Rachel"  # Voix par défaut FR si tu n’en as pas encore
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",  # Ou multilingue selon ton plan
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(
        f"{BASE_URL}/{voice}/stream",
        json=payload,
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"Erreur TTS : {response.text}")

    os.makedirs("audio", exist_ok=True)
    filename = f"audio/{uuid.uuid4()}.mp3"
    with open(filename, "wb") as f:
        f.write(response.content)

    return filename
