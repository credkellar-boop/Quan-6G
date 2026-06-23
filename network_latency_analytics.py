import numpy as np

class LatencyAnalyzer:
    def __init__(self, window_size=100):
        self.history = []
        self.window = window_size

    def log_latency(self, latency_ms):
        self.history.append(latency_ms)
        if len(self.history) > self.window:
            self.history.pop(0)

    def get_stats(self):
        return {
            "mean": np.mean(self.history),
            "jitter": np.std(self.history),
            "max": np.max(self.history)
        }

if __name__ == "__main__":
    analyzer = LatencyAnalyzer()
    analyzer.log_latency(1.2)
    analyzer.log_latency(1.5)
    print(f"Stats: {analyzer.get_stats()}")
  
