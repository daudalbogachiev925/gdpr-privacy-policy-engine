import pytest
from datetime import datetime, timedelta

from src.models import Policy
from src.engine import enforce_policy

def _make_timestamp(days_ago: int) -> str:
    dt = datetime.utcnow() - timedelta(days=days_ago)
    return dt.isoformat()

def test_enforce_required_missing():
    policy = Policy(name="req", required_fields=["user_id"])
    data = {}
    assert not enforce_policy(data, policy)

def test_enforce_prohibited_present():
    policy = Policy(name="prov", prohibited_fields=["ssn"])
    data = {"ssn": "123-45-6789"}
    assert not enforce_policy(data, policy)

def test_enforce_retention_ok():
    policy = Policy(name="ret", retention_days=10)
    data = {"timestamp": _make_timestamp(days_ago=5)}
    assert enforce_policy(data, policy)

def test_enforce_retention_expired():
    policy = Policy(name="ret", retention_days=10)
    data = {"timestamp": _make_timestamp(days_ago=15)}
    assert not enforce_policy(data, policy)

def test_enforce_all_pass():
    policy = Policy(
        name="all",
        required_fields=["id", "email"],
        prohibited_fields=["ssn"],
        retention_days=30,
    )
    data = {
        "id": "u1",
        "email": "user@example.com",
        "timestamp": _make_timestamp(days_ago=1),
    }
    assert enforce_policy(data, policy)
