class SafetyGate:
    def __init__(self, max_pos=1000):
        self.max_pos = max_pos

    def validate_order(self, qty, current_pos):
        if (current_pos + qty) > self.max_pos:
            return False, "Exceeds Position Limit"
        return True, "Approved"

if __name__ == "__main__":
    gate = SafetyGate()
    status, msg = gate.validate_order(500, 600)
    print(f"Order Status: {msg}")
  
