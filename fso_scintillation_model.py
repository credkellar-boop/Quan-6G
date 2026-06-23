import math

class ScintillationModel:
    def __init__(self, wavelength_nm=1550):
        self.k = (2 * math.pi) / (wavelength_nm * 1e-9)

    def calculate_variance(self, cn2, distance_km):
        # Rytov variance for weak turbulence
        L = distance_km * 1000
        return 1.23 * (self.k ** (7/6)) * cn2 * (L ** (11/6))

if __name__ == "__main__":
    model = ScintillationModel()
    var = model.calculate_variance(cn2=1e-14, distance_km=5)
    print(f"Rytov Variance: {var:.4f}")
  
