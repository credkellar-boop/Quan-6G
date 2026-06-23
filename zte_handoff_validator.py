import hmac
import hashlib
import time

class SecureHandoffValidator:
    def __init__(self, pre_shared_core_key: bytes):
        self.secret_key = pre_shared_core_key

    def generate_handoff_token(self, device_id: str, target_rat: str) -> dict:
        timestamp = str(int(time.time())).encode()
        payload = f"{device_id}:{target_rat}".encode() + timestamp
        signature = hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()
        return {"payload": payload.decode(), "signature": signature}

    def verify_handoff_token(self, token_data: dict, window_seconds=30) -> bool:
        try:
            payload = token_data["payload"].encode()
            received_sig = token_data["signature"]
            timestamp = int(payload.decode().split(":")[-1])
            
            if int(time.time()) - timestamp > window_seconds:
                return False 
                
            expected_sig = hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()
            return hmac.compare_digest(expected_sig, received_sig)
        except Exception:
            return False

if __name__ == "__main__":
    validator = SecureHandoffValidator(b"SGIN_Core_Secret_Auth_Key_Vector")
    token = validator.generate_handoff_token("Device_Node_01", "5G_gNB")
    print(f"Handoff Token Verification Status: {validator.verify_handoff_token(token)}")
  
