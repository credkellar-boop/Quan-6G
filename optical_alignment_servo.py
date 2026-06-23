class BeamSteeringServo:
    def __init__(self):
        self.x, self.y = 0.0, 0.0

    def adjust(self, error_x, error_y):
        self.x += error_x * 0.1 # PID proportional gain
        self.y += error_y * 0.1
        print(f"[Servo] Alignment adjusted to: {self.x}, {self.y}")

if __name__ == "__main__":
    servo = BeamSteeringServo()
    servo.adjust(0.05, -0.02)
  
