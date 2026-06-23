import pytest
import sys
import os

# Ensure the project root is in the path so we can import your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from sgin_modules.hft_safety_gate import SafetyGate

def test_safety_gate_rejection():
    # Setup a gate with a max position of 1000
    gate = SafetyGate(max_pos=1000)
    
    # Try to add 1500 (should be rejected)
    allowed, msg = gate.validate_order(1500, 0)
    
    assert allowed is False
    assert "Exceeds Position Limit" in msg
  
