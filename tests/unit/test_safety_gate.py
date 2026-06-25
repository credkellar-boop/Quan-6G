import pytest
from hft_safety_gate import SafetyGate

def test_safety_gate_rejection():
    # Setup a gate with a max position of 1000
    gate = SafetyGate(max_pos=1000)

    # Try to add 1500 (should be rejected)
    allowed, msg = gate.validate_order(1500, 0)

    assert allowed is False
    assert "Exceeds Position Limit" in msg
