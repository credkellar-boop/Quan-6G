class SGINInterface:
    def query_status(self):
        return {"system": "OPERATIONAL", "latency": "0.4ms"}

if __name__ == "__main__":
    api = SGINInterface()
    print(api.query_status())

import grpc
from concurrent import futures
import api_gateway_pb2
import api_gateway_pb2_grpc
from sgin_main_orchestrator import HardwareFactory

class NOBServicer(api_gateway_pb2_grpc.NOBControlServicer):
    def SwitchHardware(self, request, context):
        print(f"[NOB] Received hardware switch: {request.hardware_type}")
        try:
            # Re-instantiate hardware using our factory
            new_hw = HardwareFactory.get_frontend(request.hardware_type)
            new_hw.configure(freq=3500, bw=100)
            return api_gateway_pb2.CommandResponse(success=True, message="Switch Successful")
        except Exception as e:
            return api_gateway_pb2.CommandResponse(success=False, message=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    api_gateway_pb2_grpc.add_NOBControlServicer_to_server(NOBServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("[NOB] Gateway active on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    
