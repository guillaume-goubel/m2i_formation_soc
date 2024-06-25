import utils


# 1 DATA FORMAT
utils.create_temp_logs_file()

while True:

    operation_choice = input(f"""
        1. Afficher le fichier log ?
        2. Check service ou port ?
        0. EXIT ?
      """)
        
    match operation_choice:
        case '1':
            response = utils.read_log_file(utils.log_file_temp).to_string(index=False)
            print(response)  
            
        case '2':
            check_choice = input("Que voulez-vous tester (service ou -s / port ou -p) ? >> ")
            response = utils.check_security_choice(check_choice)
            print(response)      
              
        case _:
            break
        