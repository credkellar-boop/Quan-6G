import socket

class SGINTransport:
    def __init__(self, target_ip="127.0.0.1", port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target = (target_ip, port)

    def send_frame(self, binary_data):
        self.sock.sendto(binary_data, self.target)

if __name__ == "__main__":
    transport = SGINTransport()
    transport.send_frame(b"\x00\x01\x02\x03") # Sample payload
