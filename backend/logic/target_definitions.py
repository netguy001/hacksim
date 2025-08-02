import random

def get_targets():
    """Return a list of dummy target systems for simulation"""
    target_systems = [
        {
            "name": "Web Server (DMZ)",
            "ip": "10.0.1.100",
            "type": "web_server",
            "os": "Ubuntu 20.04",
            "services": ["HTTP:80", "HTTPS:443", "SSH:22"],
            "criticality": "high",
            "patch_level": "outdated"
        },
        {
            "name": "Database Server",
            "ip": "10.0.2.50",
            "type": "database",
            "os": "Windows Server 2019",
            "services": ["MySQL:3306", "RDP:3389"],
            "criticality": "critical",
            "patch_level": "current"
        },
        {
            "name": "File Server",
            "ip": "10.0.2.75",
            "type": "file_server",
            "os": "Windows Server 2016",
            "services": ["SMB:445", "FTP:21"],
            "criticality": "medium",
            "patch_level": "outdated"
        },
        {
            "name": "Domain Controller",
            "ip": "10.0.2.10",
            "type": "domain_controller",
            "os": "Windows Server 2022",
            "services": ["LDAP:389", "Kerberos:88", "DNS:53"],
            "criticality": "critical",
            "patch_level": "current"
        },
        {
            "name": "Email Server",
            "ip": "10.0.1.200",
            "type": "email_server",
            "os": "CentOS 8",
            "services": ["SMTP:25", "IMAP:993", "POP3:995"],
            "criticality": "high",
            "patch_level": "partially_updated"
        },
        {
            "name": "Workstation-001",
            "ip": "10.0.3.100",
            "type": "workstation",
            "os": "Windows 11",
            "services": ["RDP:3389"],
            "criticality": "low",
            "patch_level": "current"
        }
    ]
    
    # Randomize the order and select a subset for variety
    random.shuffle(target_systems)
    num_targets = random.randint(3, len(target_systems))
    
    return target_systems[:num_targets]

def get_network_topology():
    """Return dummy network topology information"""
    return {
        "subnets": [
            {"name": "DMZ", "range": "10.0.1.0/24", "description": "Demilitarized Zone"},
            {"name": "Internal", "range": "10.0.2.0/24", "description": "Internal Corporate Network"},
            {"name": "Workstations", "range": "10.0.3.0/24", "description": "User Workstations"}
        ],
        "security_controls": [
            {"type": "firewall", "location": "perimeter", "status": "active"},
            {"type": "ids", "location": "internal", "status": "active"},
            {"type": "antivirus", "location": "endpoints", "status": "active"},
            {"type": "web_filter", "location": "proxy", "status": "active"}
        ]
    }

def get_target_vulnerabilities(target_ip):
    """Get known vulnerabilities for a specific target"""
    vulnerabilities = [
        {
            "cve": "CVE-2023-12345",
            "severity": "high",
            "description": "Remote code execution vulnerability",
            "exploitable": True
        },
        {
            "cve": "CVE-2024-67890",
            "severity": "medium",
            "description": "Information disclosure vulnerability",
            "exploitable": False
        },
        {
            "cve": "CVE-2024-11111",
            "severity": "critical",
            "description": "Privilege escalation vulnerability",
            "exploitable": True
        }
    ]
    
    # Return a random subset of vulnerabilities
    num_vulns = random.randint(0, len(vulnerabilities))
    return random.sample(vulnerabilities, num_vulns)
