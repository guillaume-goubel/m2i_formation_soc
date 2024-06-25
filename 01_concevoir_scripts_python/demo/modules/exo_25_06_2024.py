#! Exercice : Journalisation des événements de sécurité
import os
import utils

event_file = "event_file.txt"

def insert_event(date_time_format:str, event:str):

    mode = 'a'
    
    if not os.path.exists(event_file):
        mode = 'w' 
    
    with open(event_file, mode) as file:
        file.write(f"{date_time_format} - {event} \n")   
    
    print(">>> SUCCESS >>>")

while True:

    operation_choice = input(f"""                  
      
      1. Ajouter un event ?
      0. EXIT ?
                                   
      """)
    
    match operation_choice:
        case '1':
           event = input("Quel est l'évènement ? >> ")
           insert_event(utils.get_date_time_format(), event)
        case _:
            break