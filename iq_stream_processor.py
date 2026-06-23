import numpy as np

class IQProcessor:
    def process_chunk(self, iq_data):
        # Apply simple AGC (Automatic Gain Control) normalization
        return iq_data / np.sqrt(np.mean(np.abs(iq_data)**2))

if __name__ == "__main__":
    proc = IQProcessor()
    data = np.random.normal(0, 1, 1024) + 1j * np.random.normal(0, 1, 1024)
    print(f"Normalized IQ sample: {proc.process_chunk(data)[0]}")
  
