from fastapi import FastAPI
from ia import ask_gpt
from tts import generate_speech
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Agent IA Vocal prêt"}

@app.get("/test-ia")
def test_ia():
    phase = "introduction"
    prospect_input = "Oui, c'est moi-même le dirigeant."

    gpt_response = ask_gpt(phase, prospect_input)
    audio_path = generate_speech(gpt_response)
    return {
        "phase": phase,
        "prospect_input": prospect_input,
        "réponse_ia": gpt_response,
        "audio": audio_path
    }
