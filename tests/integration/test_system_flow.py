def test_engine_writes_to_buffer(shared_memory_buffer, mock_sdr):
    """
    This test uses the global shared_memory and global mock_sdr
    automatically injected by pytest.
    """
    # Use the shared_memory_buffer fixture
    shared_memory_buffer.write(b"MARKET_DATA_CHUNK")
    
    # Use the mock_sdr fixture
    mock_sdr.transmit(b"TX_DATA")
    
    # Assertions
    assert shared_memory_buffer.read(17) == b"MARKET_DATA_CHUNK"
    mock_sdr.transmit.assert_called_with(b"TX_DATA")
  
