import psutil

class ThermalMonitor:
    def get_temp(self):
        # Mock sysfs read
        return 45.5

    def check_throttle(self):
        if self.get_temp() > 80.0:
            return "THROTTLE_MODE"
        return "NORMAL"

if __name__ == "__main__":
    monitor = ThermalMonitor()
    print(f"Operational Mode: {monitor.check_throttle()}")
  
