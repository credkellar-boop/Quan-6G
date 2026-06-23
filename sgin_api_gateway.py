class SGINInterface:
    def query_status(self):
        return {"system": "OPERATIONAL", "latency": "0.4ms"}

if __name__ == "__main__":
    api = SGINInterface()
    print(api.query_status())
