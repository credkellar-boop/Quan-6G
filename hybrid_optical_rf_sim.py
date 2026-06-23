import math

class HybridOpticalRFLink:
    def __init__(self, distance_km=5.0, rf_freq_ghz=28.0, optical_wavelength_nm=1550):
        self.distance = distance_km
        self.rf_freq = rf_freq_ghz
        self.optical_wavelength = optical_wavelength_nm
        
    def calculate_rf_path_loss(self, rain_rate_mm_h):
        fspl = 20 * math.log10(self.distance) + 20 * math.log10(self.rf_freq) + 92.45
        alpha, beta = 0.187, 1.121 
        rain_attenuation = alpha * (rain_rate_mm_h ** beta) * self.distance
        return fspl + rain_attenuation

    def calculate_fso_path_loss(self, visibility_km):
        fso_base_loss = 20 * math.log10(self.distance * 1000) 
        if visibility_km <= 0:
            return float('inf')
        
        if visibility_km > 50: q = 1.6
        elif visibility_km > 6: q = 1.3
        elif visibility_km > 1: q = 0.585 * (visibility_km ** (1/3))
        else: q = 0
            
        beta_lambda = (3.91 / visibility_km) * ((self.optical_wavelength / 550) ** -q)
        fso_attenuation = 4.343 * beta_lambda * self.distance
        return fso_base_loss + fso_attenuation

    def evaluate_channels(self, rain_rate, visibility):
        rf_loss = self.calculate_rf_path_loss(rain_rate)
        fso_loss = self.calculate_fso_path_loss(visibility)
        primary_link = "FSO" if fso_loss < rf_loss + 30 else "RF" 
        return {"FSO_Loss_dB": fso_loss, "RF_Loss_dB": rf_loss, "Active_Link": primary_link}

if __name__ == "__main__":
    sim = HybridOpticalRFLink()
    print(sim.evaluate_channels(rain_rate=12.5, visibility=0.8))
  
