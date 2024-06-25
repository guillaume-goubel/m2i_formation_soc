# IMPORT
import utils

while True:

    operation_choice = input(f"""
        1. Afficher le fichier log ?
        2. Afficher les connexions échouées ?
        3. Afficher les adresses IP avec plusieurs tentatives FAILED (RAPPORT)
        4. Afficher les adresses IP avec plusieurs tentatives FAILED (GRAPHE)
        5. Tester si Alerte de dépassement de plusieurs tentatives FAILED (TICKET)
        0. EXIT ?
      """)
        
    match operation_choice:
        case '1':
            response = utils.read_log_file(utils.log_file_to_read).to_string(index=False)
            print(response)  
            
        case '2':
            response = utils.failed_attempt(utils.log_file_to_read).to_string(index=False)
            print(response) 
            
        case '3':
            response = utils.get_many_ip_failed_attempt(utils.log_file_to_read, multiple_attempts=True, threshold=1).to_string(index=False)
            print(response)
            
        case '4':
            response = utils.get_many_ip_failed_attempt(utils.log_file_to_read, multiple_attempts=False, threshold=False)
            utils.get_graph(response)
            
        case '5':
            alert_level_choice = input("Quel seuil d'alerte voulez-vous tester ? >> ")
            response = utils.get_many_ip_failed_attempt(utils.log_file_to_read, multiple_attempts=True, threshold=alert_level_choice)
            for alert in utils.create_alert_message(response):
                print(alert)
            
        case _:
            break