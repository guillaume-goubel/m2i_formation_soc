import re
import os
import time
from datetime import datetime
from my_email import send_email

logs_file = "log_file.txt"

suspect_signatures = [
    (r"(?i)(\bOR\b|\bAND\b)\s*1\s*=\s*1", "SQL INJECTION: Suspicious Condition"),
    (r"(?i)\bSELECT\b.*\bFROM\b.*(\bOR\b|\bAND\b).*=.*", "SQL INJECTION: Logical Operator Usage"),
    (r"(--|;|\/\*|\*\/)", "SQL INJECTION: Suspicious Comments"),
    (r"(?i)\bUNION\b.*\bSELECT\b", "SQL INJECTION: Union Select"),
    (r"(?i)\bDROP\b.*\bTABLE\b", "SQL INJECTION: Drop Table"),
    (r"(?i)failed\s+login\s+attempt", "AUTHENTICATION: Failed Login Attempt"),
    (r"<script\b[^>]*>([\s\S]*?)<\/script>", "XSS INJECTION: XSS Injection"),
    (r"(?i)\brm\s+-rf\b", "COMMAND INJECTION: Suspicious Linux/Unix Command"),
    (r"(?i)cmd\.exe\s+\/C", "COMMAND INJECTION: Suspicious Windows Command"),
    (r"(?i)\bwget\b\s+http", "COMMAND INJECTION: Suspicious Download with wget")
]

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return [log.strip() for log in logs]

def check_threats(logs, signatures):
    threats_detected = []
    for log in logs:
        for signature, threat_type in signatures:
            if re.search(signature, log):
                threats_detected.append((log, threat_type))
                
                # print(f"Threat detected: {log} (Type: {threat_type})")
    return threats_detected

def save_threats_to_file(threats, output_file):
    output_dir = os.path.dirname("threats/"+output_file)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_file, 'w') as file:
        for threat, threat_type in threats:
            file.write(f"{threat} (Type: {threat_type})\n")
    print(f"Detected threats saved in {output_file}.")


data = read_log_file(logs_file)

while True:
    
    # DATA recovering
    threats_detected = check_threats(data, suspect_signatures)

    # DATA format
    body_message = ""
    for entry in threats_detected:
        body_message += f"{entry[0]} - {entry[1]} \\\n"

    # MAIL 
    send_email(body_message)
    
    # SAVE
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"threats/{now}_threats.txt"
    save_threats_to_file(threats_detected, output_file)

    time.sleep(2)
    print("------Scanning on progress-------")
    time.sleep(7)