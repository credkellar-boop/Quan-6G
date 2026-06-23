class HandoffPredictor:
    def predict(self, load_metrics):
        # Placeholder for inference logic
        return "HANDOFF_PROACTIVE" if load_metrics['cpu'] > 0.8 else "STAY"

if __name__ == "__main__":
    predictor = HandoffPredictor()
    print(predictor.predict({'cpu': 0.9}))
  
