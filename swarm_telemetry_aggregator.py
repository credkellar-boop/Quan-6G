class SwarmAggregator:
    def __init__(self):
        self.nodes = {}

    def update_node(self, node_id, state):
        self.nodes[node_id] = state

    def get_swarm_centroid(self):
        # Calculate geometric center of the swarm
        lats = [n['lat'] for n in self.nodes.values()]
        return sum(lats) / len(lats) if lats else 0

if __name__ == "__main__":
    swarm = SwarmAggregator()
    swarm.update_node("UAV_1", {"lat": 34.05})
    print(f"Swarm Centroid: {swarm.get_swarm_centroid()}")
  
