import subprocess
import time

class EnvironmentOrchestrator:
    def __init__(self):
        self.services = ["sdr_frontend_config.py", "sgin_main_orchestrator.py"]

    def launch_all(self):
        for service in self.services:
            print(f"[Orchestrator] Spawning {service}...")
            subprocess.Popen(["python3", service])
            time.sleep(0.5)

if __name__ == "__main__":
    orch = EnvironmentOrchestrator()
    orch.launch_all()
  
