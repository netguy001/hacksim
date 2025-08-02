from flask import Blueprint, jsonify, request
from logic.attack_engine import AttackEngine
from logic.target_definitions import get_targets
import time
import random

simulation_bp = Blueprint('simulation', __name__)

def start_simulation():
    """Main simulation function that orchestrates the attack sequence"""
    attack_engine = AttackEngine()
    targets = get_targets()
    
    # Simulate attack progression
    results = {
        "simulation_id": f"sim_{int(time.time())}",
        "status": "completed",
        "duration": random.randint(15, 45),
        "phases": [],
        "summary": {
            "total_targets": len(targets),
            "compromised": 0,
            "failed": 0,
            "critical_vulnerabilities": 0
        }
    }
    
    # Run attacks against each target
    for target in targets:
        phase_result = attack_engine.execute_attack(target)
        results["phases"].append(phase_result)
        
        if phase_result["status"] == "success":
            results["summary"]["compromised"] += 1
        else:
            results["summary"]["failed"] += 1
            
        if phase_result.get("severity") == "critical":
            results["summary"]["critical_vulnerabilities"] += 1
    
    return results

@simulation_bp.route('/start-simulation', methods=['POST'])
def start_simulation_route():
    """Endpoint to start a new cybersecurity simulation"""
    try:
        # Get optional parameters from request
        data = request.get_json() or {}
        simulation_type = data.get('type', 'standard')
        
        # Execute simulation
        simulation_results = start_simulation()
        simulation_results["type"] = simulation_type
        
        return jsonify({
            "success": True,
            "data": simulation_results,
            "message": "Simulation completed successfully"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Simulation failed to execute"
        }), 500