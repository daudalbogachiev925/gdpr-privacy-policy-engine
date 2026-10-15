from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field

class Policy(BaseModel):
    """A GDPR‑style privacy policy definition."""
    name: str
    description: Optional[str] = None
    required_fields: List[str] = Field(default_factory=list)
    prohibited_fields: List[str] = Field(default_factory=list)
    retention_days: Optional[int] = None
