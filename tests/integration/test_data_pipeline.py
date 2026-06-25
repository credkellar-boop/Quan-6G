import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Your original imports continue below:
import pytest
from sgin_modules.udp_transport_layer import UDPTransport
from sgin_modules.market_data_sink import MarketDataSink
