"""Fonctions utilitaires diverses."""

import re


def clean_text(text: str) -> str:
    """Nettoie le texte pour l'envoi à l'IA."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()
