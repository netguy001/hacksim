from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import random

logs_bp = Blueprint('logs', __name__)

def get_logs(limit=50, log_type="all"):
    """Generate dummy log entries for the simulation"""
    log_types = ["attack", "defense", "system", "alert"]
    severities = ["low", "medium", "high", "critical"]
    
    dummy_logs = []
    
    for i in range(limit):
        timestamp = datetime.now() - timedelta(minutes=random.randint(1, 1440))
        
        if log_type == "all":
            current_type = random.choice(log_types)
        else:
            current_type = log_type
            
        log_entry = {
            "id": f"log_{timestamp.strftime('%Y%m%d_%H%M%S')}_{i}",
            "timestamp": timestamp.isoformat(),
            "type": current_type,
            "severity": random.choice(severities),
            "source_ip": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            "target_ip": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "message": generate_log_message(current_type),
            "details": {
                "user_agent": "Mozilla/5.0 (compatible; HackSim/1.0)",
                "port": random.choice([22, 80, 443, 3389, 21, 23]),
                "protocol": random.choice(["TCP", "UDP", "HTTP", "HTTPS"])
            }
        }
        dummy_logs.append(log_entry)
    
    # Sort by timestamp (newest first)
    dummy_logs.sort(key=lambda x: x["timestamp"], reverse=True)
    return dummy_logs

def generate_log_message(log_type):
    """Generate realistic log messages based on type"""
    messages = {
        "attack": [
            "Brute force attempt detected on SSH service",
            "SQL injection attempt blocked",
            "Port scan detected from external source",
            "Suspicious payload in HTTP request",
            "Multiple failed login attempts"
        ],
        "defense": [
            "Firewall rule triggered - blocking malicious IP",
            "IDS signature match - potential threat neutralized",
            "Access denied - unauthorized resource request",
            "Rate limiting activated for suspicious activity",
            "Security policy violation detected and blocked"
        ],
        "system": [
            "Service restart completed successfully",
            "Configuration update applied",
            "System backup completed",
            "Memory usage threshold exceeded",
            "Network connectivity restored"
        ],
        "alert": [
            "CRITICAL: Potential data exfiltration detected",
            "WARNING: Unusual network traffic patterns",
            "INFO: Security scan completed",
            "ERROR: Authentication service temporarily unavailable",
            "NOTICE: System maintenance window approaching"
        ]
    }
    
    return random.choice(messages.get(log_type, messages["system"]))

@logs_bp.route('/logs', methods=['GET'])
def get_logs_route():
    """Endpoint to retrieve system logs"""
    try:
        # Get query parameters
        limit = int(request.args.get('limit', 50))
        log_type = request.args.get('type', 'all')
        
        # Validate parameters
        if limit > 200:
            limit = 200
            
        # Get logs
        logs_data = get_logs(limit, log_type)
        
        return jsonify({
            "success": True,
            "data": {
                "logs": logs_data,
                "total_count": len(logs_data),
                "filters_applied": {
                    "limit": limit,
                    "type": log_type
                }
            },
            "message": f"Retrieved {len(logs_data)} log entries"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to retrieve logs"
        }), 500