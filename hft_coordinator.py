import multiprocessing
import time
from ipc_ring_buffer import RingBuffer
from market_data_sink import MarketDataSink

def data_ingestion_worker(queue):
    """Simulates market data arrival and feeds both paths."""
    print("[Ingestion] Starting live feed...")
    # Setup shared memory for IPC
    ring_buffer = RingBuffer("hft_shared_mem")
    
    try:
        while True:
            # Simulated incoming tick from SGIN
            new_price = 150.00 + (time.time() % 1)
            
            # 1. Hot Path: Write to shared memory immediately
            ring_buffer.write(new_price)
            
            # 2. Cold Path: Send to queue for the logging worker
            queue.put({'ts': time.time_ns(), 'price': new_price})
            
            time.sleep(0.001) # 1kHz feed rate
    finally:
        ring_buffer.cleanup()

def logging_worker(queue):
    """Non-blocking archiver that runs on a separate CPU core."""
    sink = MarketDataSink(filename="live_capture.feather")
    print("[Logger] Archiver online.")
    while True:
        data = queue.get()
        if data is None: break # Shutdown signal
        sink.append_tick(data['ts'], data['price'], data['price'] + 0.05)

if __name__ == "__main__":
    # Create a thread-safe queue to bridge the paths
    data_queue = multiprocessing.Queue()
    
    # Spawn workers
    p1 = multiprocessing.Process(target=data_ingestion_worker, args=(data_queue,))
    p2 = multiprocessing.Process(target=logging_worker, args=(data_queue,))
    
    p1.start()
    p2.start()
    
    try:
        p1.join()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        print("\n[Coordinator] System shutdown complete.")
      
