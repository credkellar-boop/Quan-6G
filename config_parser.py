import yaml

class ConfigLoader:
    def __init__(self, config_file="sgin_config.yaml"):
        with open(config_file, 'r') as f:
            self.cfg = yaml.safe_load(f)

    def get(self, key):
        return self.cfg.get(key)

if __name__ == "__main__":
    # Ensure sgin_config.yaml exists with content
    # loader = ConfigLoader()
    # print(f"Node ID: {loader.get('node_id')}")
    pass
  
