import pytest
from unittest.mock import MagicMock
from sgin_modules.ipc_ring_buffer import RingBuffer
from sgin_modules.sdr_frontend_config import BaseSDR

@pytest.fixture(scope="session")
def shared_memory_buffer():
    """Global fixture for shared memory access."""
    buffer_name = "test_shm_global"
    # Setup: Initialize the buffer
    rb = RingBuffer(buffer_name, size=4096)
    
    yield rb # Provide the buffer to the tests
    
    # Teardown: Cleanup after tests are done
    rb.cleanup()

@pytest.fixture(scope="function")
def mock_sdr():
    """Global fixture for a virtual hardware radio."""
    mock = MagicMock(spec=BaseSDR)
    mock.transmit.return_value = True
    return mock

