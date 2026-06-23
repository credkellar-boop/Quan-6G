import os

class Watchdog:
    def check_health(self, process_id):
        if not os.path.exists(f"/proc/{process_id}"):
            print("[Watchdog] Process critical fail. Re-initializing hardware...")

if __name__ == "__main__":
    watchdog = Watchdog()
    watchdog.check_health(1234)
  
