class MECTaskOffloader:
    def __init__(self, device_cpu_hz=2e9, edge_cpu_hz=1e10):
        self.local_cpu = device_cpu_hz
        self.edge_cpu = edge_cpu_hz
        self.power_coeff = 1e-28 # Watt calculation coefficient

    def evaluate_offload(self, task_cycles, upload_size_bits, bandwidth_bps):
        # Local execution cost
        local_time = task_cycles / self.local_cpu
        local_energy = self.power_coeff * (self.local_cpu ** 2) * task_cycles

        # Edge offload cost
        transmission_time = upload_size_bits / bandwidth_bps
        edge_processing_time = task_cycles / self.edge_cpu
        total_offload_time = transmission_time + edge_processing_time
        
        # Decision
        if total_offload_time < local_time and local_energy > 0.5:
            return "OFFLOAD_TO_EDGE", total_offload_time
        return "PROCESS_LOCALLY", local_time

if __name__ == "__main__":
    mec = MECTaskOffloader()
    action, duration = mec.evaluate_offload(task_cycles=10e9, upload_size_bits=5e6, bandwidth_bps=100e6)
    print(f"MEC Decision: {action} (Est. Time: {duration:.4f}s)")
  
