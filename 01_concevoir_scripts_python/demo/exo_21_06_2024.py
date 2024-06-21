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

#! exercice set
# data_set = {"Aaron", "Achille", "Adélie", "Aedan", "Alana", "Aldric"}

# while True:
    
#     operation_choice = input(f"""
#       1. Stocker un nom ?
#       2. Afficher les noms ?
#       3. Editer un nom ?
#       4. Supprimer un nom ?
#       0. EXIT ?
#       """)
    
#     match operation_choice:
#         case '1':
#             new_name = input("quel nom voulez-vous rajouter ? >> ")
#             data_set.add(new_name.capitalize())

#         case '2':
#             print('----- LA LISTE ACTUELLE -----')
#             for i in data_set:
#                 print(i)

#         case '3':
           
#            name_in_data = input("quel nom voulez-vous éditer ? >> ")
#            new_name = input("par quel nom voulez-vous le remplacer ? >> ")
#            if name_in_data in data_set:
#                data_set.discard(name_in_data)
#                data_set.add(new_name.capitalize())

#         case '4':
#             name_in_data = input("quel nom voulez-vous supprimer ? >> ")
#             if name_in_data in data_set:
#                data_set.discard(name_in_data)
            
#         case _:
#             break

#! dictionnaire
# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
# - numéro de voie 
# - complément 
# - intitulé de voie 
# - commune 
# - code postal 
# - Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
# - Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur. 

data_streets_list = [

    {
        "num_voie": 'toto',
        "complement": 'toto',
        "voie": 'toto',
        "city": 'toto',
        "cp": 'toto',
    },
    {
        "num_voie": 'titi',
        "complement": 'titi',
        "voie": 'titi',
        "city": 'titi',
        "cp": 'titi',
    },

]

while True:
    
    operation_choice = input(f"""
      1. Ajouter une adresse ?
      2. Editer une adresse ?
      3. Supprimer une adresse ?
      4. Liste des adresses 
      0. EXIT ?
      """)
    
    match operation_choice:
        case '1':

            new_num_voie = input("numéro de voie  ? >> ")
            new_complemt = input("complément  ? >> ")
            new_street = input("intitulé de voie  ? >> ")
            new_city = input("commune  ? >> ")
            new_cp = input("code postal  ? >> ")

            new_adress = {
                "num_voie": new_num_voie,
                "complement": new_complemt,
                "voie": new_street,
                "city": new_city,
                "cp": new_cp,
            }

            data_streets_list.append(new_adress)

        case '2':
            pass

        case '3':
            pass

        case '4':
            for adresses in data_streets_list:
                for adress in adresses.values():
                    print(f" {adress['num_voie']} {adress['complement']}  {adress['num_voie']}  {adress['voie']}  {adress['city']} {adress['cp']} ")
        case _:
            break