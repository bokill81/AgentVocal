import openai
from config import OPENAI_API_KEY
from prompts import adam_identity, PHASES

openai.api_key = OPENAI_API_KEY


def ask_gpt(phase: str, user_input: str) -> str:
    phase_prompt = PHASES.get(phase, "")
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": adam_identity},
            {"role": "user", "content": f"Phase : {phase}\nScript : {phase_prompt}\nRéponse du prospect : {user_input}"},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
