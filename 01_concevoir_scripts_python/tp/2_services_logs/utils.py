import pandas as pd
import os

# DATA 
log_file_to_read = "logs_file.txt"
log_file_temp = "log_file_temp.txt"

standard_ports = [
    "80", "993", "1723", "3306", "23", "53", "21", "8080", "995", "67", 
    "69", "25", "5900", "6000", "68", "143", "110", "3389", "22", "443"
]
standard_services = [
    "http", "imaps", "pptp", "mysql", "telnet", "dns", "ftp", "http-alt", "pop3s", "dhcp", 
    "tftp", "smtp", "vnc", "x11", "dhcp", "imap", "pop3", "rdp", "ssh", "https"
]

def transform_line(line):
    parts = line.split(", ")
    
    port = parts[0].split(": ")[1]
    service = parts[1].split(": ")[1]
    status = parts[2].split(": ")[1]
    return f"{port}, {service}, {status}\n"

def create_temp_logs_file():
    
    if os.path.exists(log_file_to_read):
        with open(log_file_to_read, 'r') as file:
            lines = file.readlines()
    
        transformed_lines = [transform_line(line.strip()) for line in lines]
        
        with open(log_file_temp, 'w') as file:
            for line in transformed_lines:
                file.write(line)
    else:
        print('no logs file te read')

# FUNCTIONs
def read_log_file():
    df = pd.read_csv(log_file_temp, delimiter=',', names=["port", "service", "status"])
    return df

def check_security_choice(check_choice):
   
    if check_choice == '-s' or check_choice == 'service':
        return check_security_service()
    elif check_choice == '-p' or check_choice == 'port':
        return check_security_port()
    else:
        print("Le choix n'est pas correct : service ou -s / port ou -p ")

    
def check_security_service():
    
    data = pd.read_csv(log_file_temp, delimiter=',', names=["port", "service", "status"])
    data['service'] = data['service'].str.strip()
    data = data[~data['service'].isin(standard_services)]
    
    return data

def check_security_port():
    
    data = pd.read_csv(log_file_temp, delimiter=',', names=["port", "service", "status"], dtype={"port": str})
    data['port'] = data['port'].str.strip()
    data = data[~data['port'].isin(standard_ports)]
    
    return data

def create_alert_message(data):

    alerts= []
    
    # Itérer sur les lignes du DataFrame
    for index, row in data.iterrows():
        
        priority = ""
        port = row['port']
        service = row['service']
        status = row['status']
    
        if status.strip() == 'active':
            priority = "---------------------HIGH PRIORITY-------------------------"
 
        alert_message = (
            f"############################################################\n"
            f"{priority}\n\n"
            f"Subject: Security Alert - Non-Standard Service Detected\n"
            f"ALERT: A non-standard service has been detected on port: {port}\n"
            f"Service: {service}\n"
            f"Status: {status}\n\n"
            f"Immediate action is required. Please investigate the suspicious activity related to this service.\n"
            f"Ensure that the service {row.service} is verified and review access logs for any further anomalies.\n\n"
            f"Best regards,\n"
            f"Security Team\n"
        )
        
        alerts.append(alert_message)
        
    return alerts

def create_report(type=False):
    if type == "service":
        data = check_security_service()
        return create_alert_message(data)
    else:
        data = check_security_port()
        return create_alert_message(data)

