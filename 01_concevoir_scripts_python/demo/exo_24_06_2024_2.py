import uuid

# ! Gestion des Utilisateurs du Data Center
# data = {}

# def add_func(user_name:str, user_role:str) -> None:
    
#     data_id = str(uuid.uuid4())

#     new_data = {
#         data_id: {
#             "name": user_name,
#             "role": user_role
#         }
#     }

#     data.update(new_data)

# def edit_func(id:str):
#     if id in data:
#         role = input("quel rôle ? >> ")
#         data[id]['role'] = role
#         print(f"role modifié pour le user avec l'ID {id}.")
#     else:
#         print(f"role modifié pour le user avec l'ID {id}.")

# def list_func():

#     for key, data_infos in data.items():
#         print(f"id => {key}")
#         print(f"{data_infos['name']} : {data_infos['role']}")

#     return data

# while True:

#     operation_choice = input(f"""
#       1. Stocker un nom ?
#       2. changer le rôle ?
#       3. Liste des noms?
#       0. EXIT ?
#       """)
    
#     match operation_choice:
#         case '1':
#             name = input("quel nom ? >> ")
#             role = input("quel rôle ? >> ")
#             add_func(name, role)
            
#         case '2':
#             id = input("quel compte voulez-vous modifier => (id) ? >> ")
#             edit_func(id)

#         case '3':
#             list_func()
#         case _:
#             break
    
#! Suivi des Tâches de Maintenance
# data = []

# def add_func(name:str, status:str) -> None:
#     data_id = str(uuid.uuid4())
#     new_data = tuple([data_id, name, status])
#     data.append(new_data)

# def search_by_id(id:str):
#     key_to_edit = None
    
#     for key, data_infos in enumerate(data):
#         if data_infos[0] == id:
#             key_to_edit = key
#             break

#     return [ data[key_to_edit], key_to_edit ] 

# def change_status(task_infos:list):

#     status = input("quel statut ? >> ")

#     data[task_infos[1]] = (task_infos[0][0], task_infos[0][1], status)
#     return data


# def list_func():

#     for data_infos in data:
#         print(f"=============================================")
#         print(f"id => {data_infos[0]}")
#         print(f"{data_infos[1]} : {data_infos[2]}")

#     return data

# while True:

#     operation_choice = input(f"""
#       1. Stocker une tâche ?
#       2. changer le statut ?
#       3. Liste des statuts ?
#       0. EXIT ?
#       """)
    
#     match operation_choice:
#         case '1':
#             name = input("quelle tache ? >> ")
#             role = input("quel statut ? >> ")
#             add_func(name, role)
            
#         case '2':
#             id = input("quelle tâche voulez-vous modifier => (id) ? >> ")
#             change_status(search_by_id(id))

#         case '3':
#             list_func()
#         case _:
#             break

#! Analyse des Logs du Système
data = [
    {
        "log_code": "ERROR",
        "log_message": "Erreur système" 
    },
    {
        "log_code": "INFO",
        "log_message" : "Maintenance prévue à 23h ce soir" 
    },
    {
        "log_code": "ERROR",
        "log_message": "Échec de connexion" 
    },
    {
        "log_code": "INFO",
        "log_message" : "Mise à jour requise" 
    }
]

def filtrer_logs(data):
    
    response = []
    error_priority = input("quel type de log voulez-vous prioriser ? >> ")

    for log in data:
        if log['log_code'] == error_priority:
            response.append(log)

    response_format = log_in_view(response)
    return response_format

def log_in_view(response:list):
    for log in response:
        print(f"=============================================")
        print(f"{log['log_code']} : {log['log_message']}")

def log_counter(data):
    
    main_response = {}
    log_types = ('ERROR', 'INFO', 'WARNING')
    
    for log_type in log_types:
        main_response[log_type] = {
            "type" : log_type,
            "total" : 0
        }

    print(main_response)

    for type in main_response:
        # print(type)

        counter = 0
        for logs in data:
            # print(logs)
            if type == logs['log_code']:
                counter += 1
        
        print(counter)
        #!!! TO DO

filtrer_logs(data)
log_counter(data)














