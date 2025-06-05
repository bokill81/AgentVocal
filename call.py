"""Gestion des appels téléphoniques via Twilio."""

from typing import Optional
from twilio.rest import Client

from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN else None


def start_call(to_number: str, from_number: str, webhook_url: str) -> Optional[str]:
    """Lance un appel sortant et retourne l'identifiant de l'appel."""
    if client is None:
        raise ValueError("Twilio n'est pas configuré")
    call = client.calls.create(to=to_number, from_=from_number, url=webhook_url)
    return call.sid
