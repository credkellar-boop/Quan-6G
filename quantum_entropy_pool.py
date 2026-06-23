import os
import hashlib

class QuantumEntropyPool:
    def __init__(self, pool_size_bytes=1024):
        self.pool_size = pool_size_bytes
        self.entropy_pool = bytearray(self.pool_size)
        self._seed_pool()

    def _seed_pool(self):
        # Simulating hardware quantum noise with OS urandom for script execution
        raw_noise = os.urandom(self.pool_size)
        for i in range(self.pool_size):
            self.entropy_pool[i] ^= raw_noise[i]

    def extract_key(self, length_bytes=32):
        if length_bytes > self.pool_size:
            self._seed_pool()
            
        extracted = self.entropy_pool[:length_bytes]
        # Von Neumann debiasing / Hash-based extraction
        secure_key = hashlib.sha3_256(extracted).digest()
        
        # Rotate pool
        self.entropy_pool = self.entropy_pool[length_bytes:] + os.urandom(length_bytes)
        return secure_key

if __name__ == "__main__":
    q_pool = QuantumEntropyPool()
    key = q_pool.extract_key()
    print(f"Generated Quantum-Secured Key: {key.hex()}")
  
