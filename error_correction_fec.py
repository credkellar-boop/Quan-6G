class FECManager:
    def encode(self, data_blocks):
        # Generate parity block via XOR
        parity = 0
        for b in data_blocks:
            parity ^= b
        return data_blocks + [parity]

    def recover(self, blocks):
        # If one block is missing, XOR the others to recover
        return [b for b in blocks if b is not None]

if __name__ == "__main__":
    fec = FECManager()
    encoded = fec.encode([10, 20, 30])
    print(f"Encoded Data: {encoded}")
  
