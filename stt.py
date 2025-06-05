import asyncio
import json
import sounddevice as sd
import websockets

from config import DEEPGRAM_API_KEY

SAMPLE_RATE = 16000
CHUNK_DURATION = 0.5  # secondes
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)


async def send_audio(ws):
    def callback(indata, frames, time, status):
        if status:
            print("⚠️", status)
        audio_bytes = indata.tobytes()
        message = {
            "type": "Binary",
            "data": audio_bytes.decode('latin1'),
        }
        asyncio.run_coroutine_threadsafe(ws.send(json.dumps(message)), asyncio.get_event_loop())

    with sd.InputStream(channels=1, samplerate=SAMPLE_RATE, dtype='int16', blocksize=CHUNK_SIZE, callback=callback):
        print("🎙️ Nicolas est à l’écoute... (Ctrl+C pour arrêter)")
        while True:
            await asyncio.sleep(0.1)


async def receive_transcription(ws):
    async for message in ws:
        print("🗣️ Réponse brute Deepgram :", message)


async def listen_and_transcribe():
    uri = "wss://api.deepgram.com/v1/listen?language=fr&encoding=linear16&sample_rate=16000"
    headers = {"Authorization": f"Token {DEEPGRAM_API_KEY}"}
    async with websockets.connect(uri, extra_headers=headers) as ws:
        await asyncio.gather(send_audio(ws), receive_transcription(ws))


if __name__ == "__main__":
    asyncio.run(listen_and_transcribe())
