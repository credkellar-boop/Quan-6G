class MultiRATHandoffController:
    def __init__(self):
        self.weights = [0.4, 0.3, 0.1, 0.2]
        
    def normalize_metrics(self, networks):
        normalized = {}
        for rat, metrics in networks.items():
            norm_bw = metrics['bw'] / 1000.0 
            norm_lat = 1.0 / (metrics['latency'] + 1)
            norm_jit = 1.0 / (metrics['jitter'] + 1)
            norm_cost = 1.0 / (metrics['cost'] + 1)
            normalized[rat] = [norm_bw, norm_lat, norm_jit, norm_cost]
        return normalized

    def select_network(self, current_profiles):
        norm_data = self.normalize_metrics(current_profiles)
        best_rat = None
        highest_score = -1
        
        for rat, metrics in norm_data.items():
            score = sum(m * w for m, w in zip(metrics, self.weights))
            if score > highest_score:
                highest_score = score
                best_rat = rat
        return best_rat, highest_score

if __name__ == "__main__":
    profiles = {
        '4G_LTE':  {'bw': 50,  'latency': 45, 'jitter': 5,  'cost': 1},
        '5G_gNB':  {'bw': 400, 'latency': 12, 'jitter': 2,  'cost': 3},
        '6G_THz':  {'bw': 2500,'latency': 2,  'jitter': 1,  'cost': 7}
    }
    controller = MultiRATHandoffController()
    selected, score = controller.select_network(profiles)
    print(f"Target: {selected} | Score: {score:.4f}")
  
