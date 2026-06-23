import math

class LEOTracker:
    def __init__(self, altitude_km=550):
        self.earth_radius_km = 6371.0
        self.g_constant = 6.67430e-11
        self.earth_mass = 5.972e24
        self.radius_m = (self.earth_radius_km + altitude_km) * 1000

    def calculate_orbital_velocity(self):
        velocity_mps = math.sqrt((self.g_constant * self.earth_mass) / self.radius_m)
        return velocity_mps / 1000  # Convert to km/s

    def line_of_sight_window(self, ground_station_lat, ground_station_lon, sat_lat, sat_lon):
        # Simplified Haversine for line of sight
        dlat = math.radians(sat_lat - ground_station_lat)
        dlon = math.radians(sat_lon - ground_station_lon)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(ground_station_lat)) * \
            math.cos(math.radians(sat_lat)) * math.sin(dlon/2)**2
        distance_radians = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance_km = self.earth_radius_km * distance_radians
        
        # Max theoretical LOS at 550km is ~2600km
        in_view = distance_km <= 2600
        return in_view, distance_km

if __name__ == "__main__":
    tracker = LEOTracker(altitude_km=550)
    print(f"Orbital Velocity: {tracker.calculate_orbital_velocity():.2f} km/s")
    in_view, dist = tracker.line_of_sight_window(34.05, -118.24, 35.10, -119.00)
    print(f"Satellite in view: {in_view} (Distance: {dist:.2f} km)")
  
