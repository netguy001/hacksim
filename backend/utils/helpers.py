import hashlib
import random
import string
from datetime import datetime, timedelta

def generate_session_id():
    """Generate a unique session identifier"""
    timestamp = str(int(datetime.now().timestamp()))
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"session_{timestamp}_{random_string}"

def hash_string(input_string):
    """Generate SHA-256 hash of input string"""
    return hashlib.sha256(input_string.encode()).hexdigest()

def format_timestamp(timestamp=None):
    """Format timestamp for logging"""
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S UTC")

def generate_ip_address(subnet="10.0"):
    """Generate a random IP address within a subnet"""
    return f"{subnet}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def calculate_risk_score(vulnerabilities, target_criticality):
    """Calculate a risk score based on vulnerabilities and target criticality"""
    base_scores = {
        "low": 1,
        "medium": 3,
        "high": 7,
        "critical": 10
    }
    
    criticality_multiplier = {
        "low": 1.0,
        "medium": 1.5,
        "high": 2.0,
        "critical": 3.0
    }
    
    vuln_score = sum(base_scores.get(vuln.get("severity", "low"), 1) for vuln in vulnerabilities)
    multiplier = criticality_multiplier.get(target_criticality, 1.0)
    
    final_score = min(vuln_score * multiplier, 100)  # Cap at 100
    return round(final_score, 1)

def simulate_network_delay():
    """Simulate realistic network delay for operations"""
    return random.uniform(0.1, 2.0)

def generate_random_port():
    """Generate a random port number"""
    common_ports = [22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3389, 5432, 3306]
    return random.choice(common_ports + [random.randint(1024, 65535)])

def mask_sensitive_data(data, mask_char="*"):
    """Mask sensitive information in strings"""
    if len(data) <= 4:
        return mask_char * len(data)
    
    visible_chars = 2
    masked_section = mask_char * (len(data) - visible_chars * 2)
    return data[:visible_chars] + masked_section + data[-visible_chars:]

def validate_ip_address(ip):
    """Basic IP address validation"""
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        
        return True
    except (ValueError, AttributeError):
        return False

def get_severity_color(severity):
    """Get color code for severity levels (for terminal output)"""
    colors = {
        "low": "\033[92m",      # Green
        "medium": "\033[93m",   # Yellow
        "high": "\033[91m",     # Red
        "critical": "\033[95m"  # Magenta
    }
    return colors.get(severity.lower(), "\033[0m")  # Default to reset