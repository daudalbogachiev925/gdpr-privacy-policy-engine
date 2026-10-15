from __future__ import annotations

from datetime import datetime
from typing import Dict

from .models import Policy

def enforce_policy(data: Dict, policy: Policy) -> bool:
    """Validate *data* against *policy*.

    Returns ``True`` if the data complies with the policy, otherwise ``False``.
    """
    # 1. Required fields must exist
    for field in policy.required_fields:
        if field not in data:
            return False

    # 2. Prohibited fields must NOT exist
    for field in policy.prohibited_fields:
        if field in data:
            return False

    # 3. Retention check – data must contain an ISO‑8601 ``timestamp`` field
    if policy.retention_days is not None:
        timestamp = data.get("timestamp")
        if not timestamp:
            return False
        try:
            ts = datetime.fromisoformat(timestamp)
        except Exception:
            # Invalid timestamp format
            return False
        age_days = (datetime.utcnow() - ts).days
        if age_days > policy.retention_days:
            return False

    return True
