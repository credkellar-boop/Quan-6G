import networkx as nx

class TopologyMapper:
    def __init__(self):
        self.graph = nx.Graph()

    def add_connection(self, u, v, latency):
        self.graph.add_edge(u, v, weight=latency)

if __name__ == "__main__":
    mapper = TopologyMapper()
    mapper.add_connection("GND_LA", "SAT_1", 2.5)
    print(f"Active Edges: {mapper.graph.edges()}")
  
