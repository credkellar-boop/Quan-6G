class SafetyGate:
    def __init__(self, max_pos=1000):
        self.max_pos = max_pos

    def validate_order(self, qty, current_pos):
        if (current_pos + qty) > self.max_pos:
            return False, "Exceeds Position Limit"
        return True, "Approved"

if __name__ == "__main__":
    gate = SafetyGate()
    status, msg = gate.validate_order(500, 600)
    print(f"Order Status: {msg}")
    
import pytest
from sgin_modules.hft_safety_gate import SafetyGate

@pytest.fixture
def risk_gate():
    return SafetyGate(max_pos=1000)

def test_safety_gate_approval(risk_gate):
    # Should approve if under limit
    allowed, msg = risk_gate.validate_order(500, 400)
    assert allowed is True
    assert "Approved" in msg

def test_safety_gate_rejection(risk_gate):
    # Should reject if over limit
    allowed, msg = risk_gate.validate_order(700, 400)
    assert allowed is False
    assert "Exceeds Position Limit" in msg
    
