#! Surveillance  de  Serveurs
# active_status = 0

# for i in range(5):
#     end_point_status = input("Définir le statut du serveur >> (a = actif & i = inactif) >> ")
#     if end_point_status == 'a':
#         active_status += 1

# print(f"Il y a { active_status } serveurs actifs et { 5 - active_status } inactifs")

#! Vérification  des  Unités  de  Stockage  avec  Tentatives  Limitées:  Un  data  center  doit  régulièrement  vérifier
# end_point_needs_maintenance = 0

# while True:
#     for i in range(1, 4):
        
#         initial_test = input(f"machine {i} , test initial  ? >> ")
        
#         if initial_test == 'ko':
            
#             for j in range(3):
#                 validation_test = input(f"machine {i} , test validation : {j}  ? >> ")
#                 if validation_test == 'ok':
#                     break
#                 if j == 2:
#                     print(f"machine {i} est en maintenance MANUELLE ")
#                     end_point_needs_maintenance += 1
#     break
# print(f" >>>> {end_point_needs_maintenance} machines ont besoin de maintenance >>>> ")

#! Vérification de la latence du réseau
# while True:
#     latence = input(f"quelle est la latence ? >> ")

#     if latence == 'stop':
#         break

#     latence_int = int(latence)

#     if latence_int > 100:
#         is_action_do = False

#         while (is_action_do == False):
#             print('ALARME !!!!!!!! >> des actions ont-elles été prises ?')
#             action = input(f"des actions ont-elles été prises ? >> ( o/n ) ")
            
#             if action == 'o':
#                 is_action_do = True
#     else:
#         break

#! Exercice list => 
# import statistics as stat

# notes_list = []
# notes_number = int(input(f"combien de notes voulez-vous renseigner ? >> "))

# for note in range(notes_number):
#     note_value = int(input(f"valeur de la note {note+1} ? >> "))
    
#     if note_value >= 0:
#         notes_list.append(note_value)
#     else:
#         print(" /!ERROR!\ - Merci de renseigner des notes positives")


# while True:
    
#     operation_choice = input(f"""
#       1. Min ?
#       2. Max ?
#       3. Moyenne ?
#       0. EXIT ?
#       """)
    
#     match operation_choice:
#         case '1':
#             print(f"La note min >> { min(notes_list) }" )  
#         case '2':
#             print(f"La note max >> { max(notes_list) }" )  
#         case '3':
#             print(f"LA NOTE MOYENNE EST >> { round(stat.mean(notes_list), 2) }" )  
#         case _:
#             break