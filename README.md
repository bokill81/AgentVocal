# AgentVocal

Prototype d'agent vocal de prospection téléphonique. Le projet utilise FastAPI pour exposer une API de test ainsi que plusieurs services externes :

- **OpenAI GPT-4** pour la génération de texte
- **ElevenLabs** pour la synthèse vocale
- **Deepgram** pour la reconnaissance vocale
- **Twilio** pour la gestion des appels (non implémenté dans cet exemple)

Les clés API doivent être placées dans un fichier `.env` à la racine :

```
OPENAI_API_KEY=...
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_ID=...
DEEPGRAM_API_KEY=...
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
```

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn main:app --reload
```

## Structure

- `ia.py` : appel à GPT-4
- `tts.py` : synthèse vocale via ElevenLabs
- `stt.py` : écoute et transcription via Deepgram
- `call.py` : modèle pour les appels Twilio
- `log.py` : journalisation simple
- `prompts.py` : définitions des scripts commerciaux
- `config.py` : lecture des variables d'environnement
