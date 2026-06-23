try:
    import uhd
except ImportError:
    uhd = None

def initialize_sdr_frontend(device_addr="addr=192.168.10.2", center_freq=3.5e9, sample_rate=100e6, gain=35):
    if not uhd:
        return "ERROR: UHD binding missing. Install uhd Python API to interface with hardware."
        
    usrp = uhd.usrp.MultiUSRP(device_addr)
    usrp.set_rx_rate(sample_rate, 0)
    usrp.set_rx_freq(uhd.libpyuhd.types.tune_request(center_freq), 0)
    usrp.set_rx_gain(gain, 0)
    usrp.set_rx_bandwidth(sample_rate, 0)
    
    return {
        "status": "Initialized",
        "frequency_hz": usrp.get_rx_freq(0),
        "actual_rate_sps": usrp.get_rx_rate(0)
    }

if __name__ == "__main__":
    print(initialize_sdr_frontend())
  
