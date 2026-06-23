import pytest
from unittest.mock import MagicMock
from sgin_modules.hft_integrated_engine import HFTIntegratedEngine
from sgin_modules.sdr_frontend_config import BaseSDR

# A Mock SDR to simulate the hardware interface
class MockSDR(BaseSDR):
    def transmit(self, data):
        return True
    
    def receive_packet(self):
        # Simulate a raw market data packet
        return b"\xDE\xAD\xBE\xEF" 

def test_radio_to_engine_handshake():
    # 1. Setup
    mock_radio = MockSDR()
    engine = HFTIntegratedEngine(frontend=mock_radio)
    
    # 2. Execution
    # Simulate the engine pulling a packet from the "radio"
    data = engine.process_incoming_packet()
    
    # 3. Assertion
    # Check that the engine actually received the data from the mock
    assert data == b"\xDE\xAD\xBE\xEF"
    assert engine.status == "PROCESSING"

def test_engine_rejects_bad_data():
    # This tests how the engine reacts if the radio sends corrupted data
    mock_radio = MockSDR()
    mock_radio.receive_packet = MagicMock(return_value=None) # Simulate signal loss
    
    engine = HFTIntegratedEngine(frontend=mock_radio)
    data = engine.process_incoming_packet()
    
    assert data is None
    assert engine.status == "IDLE"
  
