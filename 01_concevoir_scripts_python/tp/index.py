# IMPORT
import utils

while True:

    operation_choice = input(f"""
        1. Rendre le fichier log ?
        2. Rendre les connexions échouées ?
        3. Rendre les adresses IP avec plusieurs tentatives (RAPPORT)
        0. EXIT ?
      """)
        
    match operation_choice:
        case '1':
            print(utils.read_log_file(utils.log_file_to_read))  
        case '2':
            print(utils.failed_attempt(utils.log_file_to_read))  
        case '3':
            utils.get_many_ip_failed_attempt(utils.log_file_to_read)
        case _:
            break