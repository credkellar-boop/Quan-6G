class LowLatencyEdgeRouter:
    def __init__(self):
        self.speed_of_light_vacuum = 299792.458 # km/s
        self.speed_of_light_fiber = 200000.0 # km/s (approx in silica)

    def route_hft_payload(self, distance_km, is_geo_arbitrage=False):
        # Terrestrial routing involves switching delays (approx 5ms baseline + propagation)
        terrestrial_delay_ms = (distance_km / self.speed_of_light_fiber) * 1000 + 5.0
        
        # SGIN routing involves up/downlink to LEO (550km x 2) + vacuum laser routing
        leo_distance = distance_km + (550 * 2)
        sgin_delay_ms = (leo_distance / self.speed_of_light_vacuum) * 1000 + 1.5 # Lower switching delay
        
        route = "SGIN_LEO" if sgin_delay_ms < terrestrial_delay_ms else "TERRESTRIAL_FIBER"
        
        return {
            "selected_route": route,
            "terrestrial_rtt_ms": terrestrial_delay_ms * 2,
            "sgin_rtt_ms": sgin_delay_ms * 2
        }

if __name__ == "__main__":
    router = LowLatencyEdgeRouter()
    # E.g., Routing a node sync from NY to London (~5500 km)
    decision = router.route_hft_payload(5500.0)
    print(f"Optimal Node Route: {decision['selected_route']} | SGIN RTT: {decision['sgin_rtt_ms']:.2f}ms vs Fiber RTT: {decision['terrestrial_rtt_ms']:.2f}ms")
  
