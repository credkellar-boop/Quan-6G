import time
import threading

class HeartbeatMonitor:
    def __init__(self):
        self.peers = {"SAT_A": time.time(), "GND_NY": time.time()}

    def record_heartbeat(self, node_id):
        self.peers[node_id] = time.time()

    def get_stale_nodes(self, timeout=5.0):
        now = time.time()
        return [n for n, t in self.peers.items() if (now - t) > timeout]

if __name__ == "__main__":
    monitor = HeartbeatMonitor()
    monitor.record_heartbeat("SAT_A")
    print(f"Stale Nodes: {monitor.get_stale_nodes()}")
  
