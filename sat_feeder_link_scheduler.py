class TDMAScheduler:
    def allocate_slot(self, node_id, duration_ms):
        print(f"[Scheduler] Node {node_id} granted {duration_ms}ms slot.")

if __name__ == "__main__":
    scheduler = TDMAScheduler()
    scheduler.allocate_slot("Ground_Station_NY", 20)
  
