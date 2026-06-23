import grpc
import api_gateway_pb2
import api_gateway_pb2_grpc

def push_config_to_node(node_ip, hardware_type):
    channel = grpc.insecure_channel(f'{node_ip}:50051')
    stub = api_gateway_pb2_grpc.NOBControlStub(channel)
    
    # Send the hardware switch command
    response = stub.SwitchHardware(api_gateway_pb2.HardwareRequest(hardware_type=hardware_type))
    
    print(f"Node Response: {response.message}")

if __name__ == "__main__":
    # Push the new hardware configuration to the edge node
    push_config_to_node("192.168.1.50", "USRPFrontend")
  
