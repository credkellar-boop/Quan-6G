import math
try:
    import ephem
except ImportError:
    ephem = None

class EphemerisTracker:
    def __init__(self, ground_lat='34.0522', ground_lon='-118.2437', elevation_m=71):
        if not ephem:
            raise ImportError("The 'ephem' library is required. Run: pip install ephem")
            
        # Initialize the Ground Station (e.g., Los Angeles Edge Node)
        self.ground_station = ephem.Observer()
        self.ground_station.lat = ground_lat
        self.ground_station.lon = ground_lon
        self.ground_station.elevation = elevation_m
        
    def load_satellite_tle(self, name, line1, line2):
        """Loads NORAD Two-Line Element (TLE) data for precise tracking."""
        self.satellite = ephem.readtle(name, line1, line2)

    def compute_telemetry(self, timestamp=None):
        """Calculates precise azimuth, altitude, and range at a given timestamp."""
        if timestamp:
            self.ground_station.date = timestamp
        else:
            self.ground_station.date = ephem.now()
            
        self.satellite.compute(self.ground_station)
        
        # Convert ephem radian outputs to degrees
        azimuth = math.degrees(self.satellite.az)
        elevation = math.degrees(self.satellite.alt)
        
        # Determine if the satellite is currently above the horizon (LOS acquired)
        los_active = elevation > 0 
        
        return {
            "satellite_name": self.satellite.name,
            "timestamp_utc": str(self.ground_station.date),
            "azimuth_deg": round(azimuth, 4),
            "elevation_deg": round(elevation, 4),
            "range_velocity": self.satellite.range_velocity, # meters per second
            "los_active": los_active
        }

if __name__ == "__main__":
    if ephem:
        tracker = EphemerisTracker()
        
        # Sample TLE data for a generic Starlink LEO satellite
        starlink_name = "STARLINK-1007"
        tle_line_1 = "1 44713U 19074A   23281.50000000  .00001500  00000-0  10842-3 0  9997"
        tle_line_2 = "2 44713  53.0530 156.4020 0001300  86.1020 274.0010 15.06390000216000"
        
        tracker.load_satellite_tle(starlink_name, tle_line_1, tle_line_2)
        
        print("=== Ephemeris Tracking Engine Initialized ===")
        telemetry = tracker.compute_telemetry()
        
        for key, value in telemetry.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("Install 'ephem' to run the ephemeris tracker.")
      
