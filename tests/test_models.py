import pytest
from src.models import Policy

def test_policy_minimal():
    p = Policy(name="test")
    assert p.name == "test"
    assert p.required_fields == []
    assert p.prohibited_fields == []
    assert p.retention_days is None

def test_policy_full():
    p = Policy(
        name="full",
        description="Full policy",
        required_fields=["a", "b"],
        prohibited_fields=["c"],
        retention_days=30,
    )
    assert p.description == "Full policy"
    assert p.required_fields == ["a", "b"]
    assert p.prohibited_fields == ["c"]
    assert p.retention_days == 30
