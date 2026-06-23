import socket
import time
import threading

class NetworkStressTester:
    def __init__(self, target_ip="127.0.0.1", target_port=9999):
        self.target = (target_ip, target_port)
        self.is_running = False

    def _flood_worker(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = b"SGIN_STRESS_TEST_PACKET_OVERLOAD" * 32
        while self.is_running:
            try:
                sock.sendto(payload, self.target)
            except Exception:
                pass

    def run_stress_test(self, threads=5, duration_seconds=3):
        print(f"Initiating traffic load generation on {self.target[0]}:{self.target[1]}...")
        self.is_running = True
        thread_list = []
        
        for _ in range(threads):
            t = threading.Thread(target=self._flood_worker)
            t.start()
            thread_list.append(t)
            
        time.sleep(duration_seconds)
        self.is_running = False
        
        for t in thread_list:
            t.join()
        print("Stress validation complete. Check edge node telemetry for dropped packets.")

if __name__ == "__main__":
    tester = NetworkStressTester()
    tester.run_stress_test()
  
