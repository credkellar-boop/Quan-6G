import json

class ConfigSync:
    def push_config(self, node_id, new_config):
        # Serialize and send config
        payload = json.dumps(new_config)
        print(f"[Sync] Pushing config to {node_id}: {payload}")

if __name__ == "__main__":
    syncer = ConfigSync()
    syncer.push_config("EDGE_NODE_05", {"max_pos": 5000})
  
