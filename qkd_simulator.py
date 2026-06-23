import math

class QKDSimulator:
    def __init__(self, pulse_rate_mhz=100, fiber_loss_db_per_km=0.2):
        self.f_clock = pulse_rate_mhz * 1e6
        self.loss_coeff = fiber_loss_db_per_km

    def estimate_key_rate(self, distance_km, detector_efficiency=0.15, qber_baseline=0.02):
        channel_loss_db = self.loss_coeff * distance_km
        transmittance = 10 ** (-channel_loss_db / 10)
        
        raw_rate = self.f_clock * transmittance * detector_efficiency * 0.5
        error_correction_overhead = 1.2
        
        if qber_baseline >= 0.11: 
            return 0.0, qber_baseline
            
        h_e = - (qber_baseline * math.log2(qber_baseline) + (1 - qber_baseline) * math.log2(1 - qber_baseline))
        secret_rate = raw_rate * (1 - (error_correction_overhead * h_e) - h_e)
        
        return max(0.0, secret_rate), qber_baseline

if __name__ == "__main__":
    qkd = QKDSimulator()
    key_rate, error_rate = qkd.estimate_key_rate(distance_km=25)
    print(f"Secret Key Rate: {key_rate / 1000:.2f} kbps | QBER: {error_rate * 100}%")
  
