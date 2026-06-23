import time

class TimeSyncManager:
    def __init__(self):
        self.offset = 0.0

    def sync_to_pps(self, hardware_signal):
        # Align system time to the nanosecond-precision hardware PPS
        self.offset = hardware_signal - time.time_ns()
        print(f"[Clock] Sync calibrated. Offset: {self.offset}ns")

if __name__ == "__main__":
    sync = TimeSyncManager()
    sync.sync_to_pps(time.time_ns() + 150)
  
