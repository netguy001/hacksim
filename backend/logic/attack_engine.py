import random
import time
from datetime import datetime

class AttackEngine:
    """Simulates various cybersecurity attack scenarios"""
    
    def __init__(self):
        self.attack_types = [
            "port_scan", "brute_force", "sql_injection", 
            "xss_attack", "privilege_escalation", "lateral_movement",
            "data_exfiltration", "ransomware_simulation"
        ]
        
        self.vulnerabilities = [
            "CVE-2023-12345", "CVE-2023-67890", "CVE-2024-11111",
            "CVE-2024-22222", "CVE-2024-33333"
        ]
    
    def execute_attack(self, target):
        """Execute a simulated attack against a target"""
        attack_type = random.choice(self.attack_types)
        
        # Simulate attack execution time
        execution_time = random.uniform(1.5, 8.0)
        
        # Determine attack outcome (70% success rate for demo)
        success = random.random() < 0.7
        
        attack_result = {
            "target": target["name"],
            "target_ip": target["ip"],
            "attack_type": attack_type,
            "timestamp": datetime.now().isoformat(),
            "execution_time": round(execution_time, 2),
            "status": "success" if success else "failed",
            "severity": self._determine_severity(attack_type, success),
            "details": self._generate_attack_details(attack_type, target, success)
        }
        
        return attack_result
    
    def _determine_severity(self, attack_type, success):
        """Determine the severity level of the attack"""
        if not success:
            return "low"
            
        high_severity_attacks = ["privilege_escalation", "data_exfiltration", "ransomware_simulation"]
        critical_attacks = ["lateral_movement", "ransomware_simulation"]
        
        if attack_type in critical_attacks and random.random() < 0.3:
            return "critical"
        elif attack_type in high_severity_attacks:
            return "high"
        else:
            return random.choice(["medium", "high"])
    
    def _generate_attack_details(self, attack_type, target, success):
        """Generate specific details for each attack type"""
        base_details = {
            "vulnerability": random.choice(self.vulnerabilities),
            "method": self._get_attack_method(attack_type),
            "payload_size": f"{random.randint(128, 2048)} bytes"
        }
        
        if success:
            base_details.update({
                "compromised_accounts": random.randint(1, 5),
                "data_accessed": f"{random.randint(10, 500)} files",
                "persistence": random.choice(["established", "temporary", "none"])
            })
        else:
            base_details.update({
                "blocked_by": random.choice(["firewall", "ids", "antivirus", "user_awareness"]),
                "detection_time": f"{random.uniform(0.5, 30.0):.1f} seconds"
            })
        
        return base_details
    
    def _get_attack_method(self, attack_type):
        """Get the method description for each attack type"""
        methods = {
            "port_scan": "TCP SYN scan",
            "brute_force": "Dictionary attack",
            "sql_injection": "Union-based injection",
            "xss_attack": "Reflected XSS",
            "privilege_escalation": "DLL hijacking",
            "lateral_movement": "Pass-the-hash",
            "data_exfiltration": "DNS tunneling",
            "ransomware_simulation": "File encryption simulation"
        }
        
        return methods.get(attack_type, "Unknown method")
