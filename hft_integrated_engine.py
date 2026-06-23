import multiprocessing
import time
from ipc_ring_buffer import RingBuffer
from market_data_sink import MarketDataSink
from hft_safety_gate import SafetyGate

def execution_worker(shared_mem_name, safety_gate):
    """
    The 'Hot Path': Reads directly from shared memory, 
    validates via safety gate, and executes.
    """
    # Attach to existing shared memory
    ring_buffer = RingBuffer(shared_mem_name)
    
    print("[Execution] Strategy engine online. Waiting for data...")
    
    # Simulate current position state
    current_position = 500
    
    while True:
        # 1. Low-latency read from RingBuffer
        price = ring_buffer.buf[0]
        
        if price > 0:
            # 2. Safety Gate Validation (Pre-Trade)
            qty_to_trade = 100
            allowed, msg = safety_gate.validate_order(qty_to_trade, current_position)
            
            if allowed:
                # Execution logic would go here
                print(f"[Execution] Order allowed at ${price:.2f}. Logic: {msg}")
                current_position += qty_to_trade
            else:
                print(f"[Execution] Trade Rejected: {msg}")
        
        time.sleep(0.005) # Loop frequency

def data_ingestion_worker(queue, shared_mem_name):
    """The 'Cold Path' and Feed ingestion."""
    ring_buffer = RingBuffer(shared_mem_name)
    
    try:
        while True:
            # Simulated SGIN Feed
            new_price = 150.00 + (time.time() % 1)
            
            # Write to Shared Memory for the Execution engine
            ring_buffer.write(new_price)
            
            # Queue to Logger
            queue.put({'ts': time.time_ns(), 'price': new_price})
            
            time.sleep(0.001)
    finally:
        ring_buffer.cleanup()

if __name__ == "__main__":
    # Initialize Core Components
    data_queue = multiprocessing.Queue()
    shared_mem_id = "hft_shared_mem"
    safety_gate = SafetyGate(max_pos=1000)
    
    # Define Process Topology
    ingestion_proc = multiprocessing.Process(
        target=data_ingestion_worker, 
        args=(data_queue, shared_mem_id)
    )
    execution_proc = multiprocessing.Process(
        target=execution_worker, 
        args=(shared_mem_id, safety_gate)
    )
    
    # Launch
    ingestion_proc.start()
    execution_proc.start()
    
    try:
        ingestion_proc.join()
    except KeyboardInterrupt:
        print("\n[Engine] Shutting down...")
        ingestion_proc.terminate()
        execution_proc.terminate()
      
