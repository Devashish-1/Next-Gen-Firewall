import socket
import threading
import time

class MitigationEngine:
     def __init__(self, ip, port):
         self.ip = ip
         self.port = port
        #  ye function hmare ip addresses btayega ki kidr se attack ho rha hai
     def mitigate_attack(self):
         print("Mitigating attack from IP:", self.ip, "on port:", self.port)

class MitigationEngine:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.attack_count = 0
        self.last_mitigation_time = time.time()

    def mitigate_attack(self):
        print("Mitigating attack from IP:", self.ip, "on port:", self.port)
        self.attack_count += 1
        current_time = time.time()

        # agar last 10 seconds me 1000 se jyada req aati h ,then drop connections from attacker IP
        if self.attack_count > 1000 and current_time - self.last_mitigation_time < 10:
            print("Rate limiting - dropping connections from attacker's IP:", self.ip)
            self.attack_count = 0
            self.last_mitigation_time = current_time
        elif current_time - self.last_mitigation_time >= 10:
            # Attack count and mitigation ko reset krdega taki process dubara start ho
            self.attack_count = 0
            self.last_mitigation_time = current_time

a=MitigationEngine
a.__init__("175.176.187.102", "80")
a.mitigate_attack("175.176.187.102", "80")
