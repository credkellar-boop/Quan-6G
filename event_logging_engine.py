import logging

class SGINLogger:
    def __init__(self, name="SGIN_Core"):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(name)

    def log_event(self, event_type, message):
        self.logger.info(f"[{event_type}] {message}")

if __name__ == "__main__":
    logger = SGINLogger()
    logger.log_event("HARDWARE_INIT", "UHD interface locked.")
  
