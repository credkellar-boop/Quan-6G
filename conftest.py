import sys
import types
import os

# 1. VIRTUAL PACKAGING TRICK
# This maps 'sgin_modules' directly to your root folder dynamically
# so internal app imports like 'from sgin_modules.xyz' work perfectly.
sgin_modules = types.ModuleType('sgin_modules')
sgin_modules.__path__ = [os.path.abspath(os.path.dirname(__file__))]
sys.modules['sgin_modules'] = sgin_modules

# 2. MISSING FILE STUB
# Since ipc_ring_buffer.py is missing, this dynamically injects a 
# mock RingBuffer class so your integrated engine can initialize.
ipc_mock = types.ModuleType('ipc_ring_buffer')
class MockRingBuffer:
    def __init__(self, *args, **kwargs): pass
    def push(self, *args, **kwargs): pass
    def pop(self, *args, **kwargs): return b''
ipc_mock.RingBuffer = MockRingBuffer
sys.modules['ipc_ring_buffer'] = ipc_mock
