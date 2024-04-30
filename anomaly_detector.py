import numpy as np
from sklearn.ensemble import IsolationForest
class AnomalyDetector:
    def __init__(self, threshold):
        self.threshold = threshold
        self.model = IsolationForest(random_state=42)
    def detect_anomaly(self, packet_count):
        normal_data = np.random.randint(low=500, high=1500, size=(1000, 1))
        self.model.fit(normal_data)
        if self.model.predict([[packet_count]])[0] == -1:
            return True 
        else:
            return False
'''
This code defines an anomaly detector using Isolation Forest, training it on synthetic normal data and predicting anomalies based on packet counts.
'''