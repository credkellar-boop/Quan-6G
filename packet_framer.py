import struct

class PacketFramer:
    # Header: [Timestamp (Q), Sequence (I), PayloadType (B)]
    FORMAT = "!QIB"

    def frame(self, ts, seq, ptype, data):
        header = struct.pack(self.FORMAT, ts, seq, ptype)
        return header + data.encode()

if __name__ == "__main__":
    framer = PacketFramer()
    packet = framer.frame(1712345678, 1, 1, "ORDER_DATA")
    print(f"Encoded Packet: {packet.hex()}")
  
