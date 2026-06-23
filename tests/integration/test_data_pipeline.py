import pytest
from sgin_modules.udp_transport_layer import UDPTransport
from sgin_modules.market_data_sink import MarketDataSink

def test_pipeline_data_flow():
    # 1. Setup
    transport = UDPTransport(port=50051)
    sink = MarketDataSink(buffer_size=1024)
    
    # 2. Execute
    test_packet = b"\x01\x02\x03\x04"
    transport.send(test_packet)
    
    # 3. Verify that the sink actually received the packet from the transport
    received_data = sink.read_last_packet()
    
    assert received_data == test_packet
    assert sink.is_active is True
