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
def read_log_file(log_file):
    df = pd.read_csv(log_file, delimiter=',', names=["port", "service", "status"])
    return df

def check_security_choice(check_choice):
   
    if check_choice == '-s' or check_choice == 'service':
        return check_security_service(log_file_temp)
    elif check_choice == '-p' or check_choice == 'port':
        return check_security_port(log_file_temp)
    else:
        print("Le choix n'est pas correct : service ou -s / port ou -p ")

    
def check_security_service(log_file_to_read):
    
    report_df = pd.read_csv(log_file_to_read, delimiter=',', names=["port", "service", "status"])
    report_df['service'] = report_df['service'].str.strip()
    report_df = report_df[~report_df['service'].isin(standard_services)]
    
    return report_df

def check_security_port(log_file_to_read):
    
    report_df = pd.read_csv(log_file_to_read, delimiter=',', names=["port", "service", "status"], dtype={"port": str})
    report_df['port'] = report_df['port'].str.strip()
    report_df = report_df[~report_df['port'].isin(standard_ports)]
    
    return report_df

