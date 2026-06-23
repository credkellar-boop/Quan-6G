import pandas as pd

class MarketDataSink:
    def __init__(self, filename="market_capture.feather"):
        self.filename = filename
        self.buffer = []

    def append_tick(self, timestamp, bid, ask):
        self.buffer.append({'ts': timestamp, 'bid': bid, 'ask': ask})
        if len(self.buffer) > 1000:
            self.flush()

    def flush(self):
        df = pd.DataFrame(self.buffer)
        df.to_feather(self.filename)
        self.buffer = []

if __name__ == "__main__":
    sink = MarketDataSink()
    sink.append_tick(1712345678, 150.25, 150.30)
  
