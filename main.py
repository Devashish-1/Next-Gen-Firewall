from anomaly_detector import AnomalyDetector
from mitigation_engine import MitigationEngine
import config
def main():
    detector = AnomalyDetector(config.THRESHOLD)
    packet_count = 1500
    if detector.detect_anomaly(packet_count):
        engine = MitigationEngine(config.SERVER_IP, config.SERVER_PORT)
        engine.mitigate_attack()
if __name__ == "__main__":
    main()