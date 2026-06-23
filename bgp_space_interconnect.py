class SpaceGroundBGP:
    def __init__(self, asn):
        self.asn = asn
        self.routing_table = {}

    def announce_route(self, prefix, next_hop, as_path):
        # Loop prevention
        if self.asn in as_path:
            return False 
            
        new_path = [self.asn] + as_path
        self.routing_table[prefix] = {"next_hop": next_hop, "as_path": new_path}
        return True

    def display_routes(self):
        print(f"\n--- BGP Routing Table (ASN: {self.asn}) ---")
        for prefix, data in self.routing_table.items():
            print(f"Prefix: {prefix} | Next Hop: {data['next_hop']} | Path: {data['as_path']}")

if __name__ == "__main__":
    orbital_router = SpaceGroundBGP(asn=65001)
    terrestrial_router = SpaceGroundBGP(asn=65002)
    
    # Orbital router announces satellite subnet to ground
    terrestrial_router.announce_route("10.100.0.0/16", "192.168.10.1", [65001])
    terrestrial_router.display_routes()
  
