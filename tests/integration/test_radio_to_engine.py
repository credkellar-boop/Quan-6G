import pytest
from unittest.mock import MagicMock
from hft_integrated_engine import HFTIntegratedEngine
from sdr_frontend_config import BaseSDR

# A Mock SDR to simulate the hardware interface
class MockSDR(BaseSDR):
    def transmit(self, data):
        return True

    def receive_packet(self):
        # Simulate a raw market data packet
        return b'\xDE\xAD\xBE\xEF'

def test_radio_to_engine_handshake():
    # 1. Setup
    mock_radio = MockSDR()
    engine = HFTIntegratedEngine(frontend_mock_radio=mock_radio)

    # 2. Execute
    # Simulate the engine pulling a packet from the "radio"
    data = engine.process_incoming_packet()

    # 3. Assertion
    # Check that the engine actually received the data from the mock
    assert data == b'\xDE\xAD\xBE\xEF'
    assert engine.status == "PROCESSING"

def test_engine_rejects_bad_data():
    # This tests how the engine reacts if the radio sends corrupted data
    mock_radio = MockSDR()

    # Simulate signal loss by overriding the method with a mock returning None
    mock_radio.receive_packet = MagicMock(return_value=None)

    engine = HFTIntegratedEngine(frontend_mock_radio=mock_radio)
    data = engine.process_incoming_packet()

    assert data is None
    assert engine.status == "IDLE"
