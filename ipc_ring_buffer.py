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
  
