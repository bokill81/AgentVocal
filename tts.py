import os
import requests
import uuid

from config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, AUDIO_DIR

API_KEY = ELEVENLABS_API_KEY
VOICE_ID = ELEVENLABS_VOICE_ID
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"


def generate_speech(text: str) -> str:
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    voice = VOICE_ID or "Rachel"
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.8},
    }
    response = requests.post(f"{BASE_URL}/{voice}/stream", json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Erreur TTS : {response.text}")

    os.makedirs(AUDIO_DIR, exist_ok=True)
    filename = f"{AUDIO_DIR}/{uuid.uuid4()}.mp3"
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename
