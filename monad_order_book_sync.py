import threading
import time

class OrderBookSyncer:
    def __init__(self):
        # Local state: {price: quantity}
        self.bids = {}
        self.asks = {}
        self._lock = threading.Lock()

    def apply_delta(self, side, price, quantity):
        """
        Applies a delta update from the incoming SGIN stream.
        If quantity is 0, the price level is removed.
        """
        with self._lock:
            target_side = self.bids if side == 'bid' else self.asks
            
            if quantity == 0:
                target_side.pop(price, None)
            else:
                target_side[price] = quantity

    def get_top_of_book(self):
        """Returns the current Best Bid and Best Offer (BBO)."""
        with self._lock:
            best_bid = max(self.bids.keys()) if self.bids else None
            best_ask = min(self.asks.keys()) if self.asks else None
            return best_bid, best_ask

    def sync_batch(self, deltas):
        """Processes a batch of updates (e.g., from an FPGA buffer)."""
        for delta in deltas:
            self.apply_delta(delta['side'], delta['price'], delta['qty'])

# Execution Example
if __name__ == "__main__":
    sync_engine = OrderBookSyncer()
    
    # Simulate a network packet arrival
    updates = [
        {'side': 'bid', 'price': 150.25, 'qty': 100},
        {'side': 'ask', 'price': 150.30, 'qty': 150},
        {'side': 'bid', 'price': 150.25, 'qty': 0} # Cancellation
    ]
    
    sync_engine.sync_batch(updates)
    bid, ask = sync_engine.get_top_of_book()
    print(f"BBO Sync Status -> Best Bid: {bid}, Best Ask: {ask}")
  
