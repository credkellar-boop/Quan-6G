import time

class KeyRotationManager:
    def __init__(self, rotation_interval=3600):
        self.interval = rotation_interval
        self.last_rotation = time.time()

    def check_rotation_required(self):
        return (time.time() - self.last_rotation) > self.interval

if __name__ == "__main__":
    krm = KeyRotationManager(rotation_interval=10)
    print(f"Rotation Required: {krm.check_rotation_required()}")
  
