from datetime import datetime
from typing import Optional

def parse_iso_timestamp(value: str) -> Optional[datetime]:
    """Parse an ISO‑8601 timestamp string.

    Returns ``None`` if parsing fails.
    """
    try:
        return datetime.fromisoformat(value)
    except Exception:
        return None
