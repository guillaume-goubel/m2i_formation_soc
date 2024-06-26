from utils import read_log_file, check_security_choice, create_temp_logs_file, create_report

# 1 DATA FORMAT
create_temp_logs_file()

# 2 IMPLEMENTATION
while True:

    operation_choice = input(f"""
        1. Afficher le fichier log 
        2. Check service ou port ?
        3. Edition Menaces - services (RAPPORT) 
        4. Edition Menaces - port (RAPPORT) 
        0. EXIT ?
      """)
        
    match operation_choice:
        case '1':
            data = read_log_file().to_string(index=False)
            print(data)  
            
        case '2':
            check_choice = input("Que voulez-vous tester (service ou -s / port ou -p) ? >> ")
            data = check_security_choice(check_choice)
            print(data)    
            
        case '3':
            data = create_report(type="service")
            for alert in data:
                print(alert)
            
        case '4':
            data = create_report(type="port")
            for alert in data:
                print(alert)
              
        case _:
            break
        