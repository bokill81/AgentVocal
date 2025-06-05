"""Simple gestionnaire de logs textuels."""

import os
from datetime import datetime
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)


def log_message(message: str) -> None:
    filename = os.path.join(LOG_DIR, f"{datetime.utcnow().date()}.log")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.utcnow().isoformat()}] {message}\n")
