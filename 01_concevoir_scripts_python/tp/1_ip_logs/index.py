# IMPORT
from utils import read_log_file, failed_attempt, get_many_ip_failed_attempt, create_alert_message, get_graph

while True:

    operation_choice = input(f"""
        1. Afficher le fichier log
        2. Afficher les connexions échouées
        3. Afficher les adresses IP avec plusieurs tentatives FAILED (RAPPORT)
        4. Afficher les adresses IP avec plusieurs tentatives FAILED (GRAPHE)
        5. Tester si Alerte de dépassement de plusieurs tentatives FAILED (EDITION TICKET)
        0. EXIT
      """)
        
    match operation_choice:
        case '1':
            response = read_log_file().to_string(index=False)
            print(response)  
            
        case '2':
            response = failed_attempt().to_string(index=False)
            print(response) 
            
        case '3':
            response = get_many_ip_failed_attempt(multiple_attempts=True, threshold=1).to_string(index=False)
            print(response)
            
        case '4':
            response = get_many_ip_failed_attempt(multiple_attempts=False, threshold=False)
            get_graph(response)
            
        case '5':
            alert_level_choice = input("Quel seuil d'alerte voulez-vous tester ? >> ")
            response = get_many_ip_failed_attempt(multiple_attempts=True, threshold=alert_level_choice)
            for alert in create_alert_message(response):
                print(alert)
            
        case _:
            break