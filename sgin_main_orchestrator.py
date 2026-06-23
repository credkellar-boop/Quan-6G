import asyncio
import time

class SGINOrchestrator:
    def __init__(self):
        self.state = "BOOTING"
        self.modules = ["Hybrid_Sim", "Handoff_Core", "QKD_Crypt", "MEC_Offloader", "HFT_Router"]

    async def initialize_module(self, module_name):
        print(f"[Orchestrator] Spinning up {module_name}...")
        await asyncio.sleep(0.5) # Simulate hardware lock/bind time
        print(f"[Orchestrator] {module_name} ONLINE.")

    async def run_ecosystem(self):
        print("=== INITIALIZING SGIN ECOSYSTEM ===")
        tasks = [self.initialize_module(mod) for mod in self.modules]
        await asyncio.gather(*tasks)
        
        self.state = "RUNNING"
        print("\n=== SYSTEM ACTIVE. AWAITING TELEMETRY ===")
        
        try:
            while True:
                # Main orchestration heartbeat
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            self.state = "SHUTDOWN"
            print("\n[Orchestrator] Halting SGIN Ecosystem...")

if __name__ == "__main__":
    master = SGINOrchestrator()
    asyncio.run(master.run_ecosystem())
  
import importlib
import yaml
from sgin_modules.sdr_frontend_config import BaseSDR

class HardwareFactory:
    """Dynamically creates the requested hardware interface."""
    @staticmethod
    def get_frontend(class_name):
        # Dynamically import the module
        module = importlib.import_module("sgin_modules.sdr_frontend_config")
        # Get the class from the module
        frontend_class = getattr(module, class_name)
        return frontend_class()

def start_orchestrator():
    # 1. Load Configuration
    with open("sgin_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    # 2. Instantiate Hardware via Factory
    frontend_name = config['hardware']['frontend_type']
    frontend = HardwareFactory.get_frontend(frontend_name)
    
    # 3. Initialize
    frontend.configure(freq=3500, bw=100)
    
    print(f"[Orchestrator] System live using: {frontend_name}")
    # Proceed to main loop...

if __name__ == "__main__":
    start_orchestrator()
    
