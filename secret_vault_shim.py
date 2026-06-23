import os

class SecretVault:
    def get_credential(self, key_name):
        # Mock fetching from secure env
        return os.getenv(key_name, "DEFAULT_INSECURE_KEY")

if __name__ == "__main__":
    vault = SecretVault()
    print(f"Key Retrieved: {vault.get_credential('API_KEY')[:4]}***")
  
