import hashlib
import time

class NetworkConsensus:
    def __init__(self, node_id):
        self.node_id = node_id
        self.ledger = {}

    def update_state(self, link_id, status):
        timestamp = time.time()
        state_entry = f"{link_id}:{status}:{timestamp}"
        self.ledger[link_id] = hashlib.sha256(state_entry.encode()).hexdigest()
        print(f"[Node {self.node_id}] State Updated: {link_id} -> {status}")

if __name__ == "__main__":
    consensus = NetworkConsensus("Edge_Node_01")
    consensus.update_state("FSO_Link_04", "ACTIVE")
  
