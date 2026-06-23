from multiprocessing import shared_memory
import numpy as np

class RingBuffer:
    def __init__(self, name, size=1024):
        self.shm = shared_memory.SharedMemory(name=name, create=True, size=size)
        self.buf = np.ndarray((size,), dtype=np.float64, buffer=self.shm.buf)

    def write(self, data):
        self.buf[0] = data

    def cleanup(self):
        self.shm.close()
        self.shm.unlink()

if __name__ == "__main__":
    rb = RingBuffer("hft_shared_mem")
    rb.write(150.25)
    rb.cleanup()
  
import pytest
from sgin_modules.ipc_ring_buffer import RingBuffer
import multiprocessing
import time

def writer_process(name, val):
    rb = RingBuffer(name, size=1024)
    rb.write(val)
    rb.cleanup()

def test_ring_buffer_integration():
    shm_name = "test_shm_buffer"
    test_val = 150.50
    
    # Run writer in separate process
    p = multiprocessing.Process(target=writer_process, args=(shm_name, test_val))
