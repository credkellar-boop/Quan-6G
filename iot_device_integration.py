import asyncio
import time

class AutonomousDeviceNode:
    def __init__(self, device_id, device_type="UAV"):
        self.device_id = device_id
        self.device_type = device_type
        
    async def stream_telemetry(self):
        print(f"[{self.device_id}] Initializing {self.device_type} uplink...")
        try:
            while True:
                payload = {
                    "id": self.device_id,
                    "type": self.device_type,
                    "velocity_mps": 25.5,
                    "lat": 34.0522,
                    "lon": -118.2437,
                    "timestamp_ns": time.time_ns()
                }
                print(f"[{self.device_id}] Telemetry dispatched: {payload['timestamp_ns']}")
                await asyncio.sleep(0.01) 
        except KeyboardInterrupt:
            print(f"\n[{self.device_id}] Uplink terminated.")

if __name__ == "__main__":
    drone_node = AutonomousDeviceNode("Auto_Drone_01")
    asyncio.run(drone_node.stream_telemetry())
  
