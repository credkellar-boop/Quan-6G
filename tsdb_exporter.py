from prometheus_client import start_http_server, Gauge
import time

class MetricsExporter:
    def __init__(self, port=8000):
        self.latency_gauge = Gauge('sgin_network_latency_ms', 'Current network latency')
        start_http_server(port)

    def update_metrics(self, latency):
        self.latency_gauge.set(latency)

if __name__ == "__main__":
    exporter = MetricsExporter()
    while True:
        exporter.update_metrics(0.45) # Simulated latency
        time.sleep(5)
      
