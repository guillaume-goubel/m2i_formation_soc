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
from datetime import datetime

data_streets_list = {

    "094814": {
        "num_voie": '55',
        "complement": 'Entrée B',
        "voie": 'rue du Faubourg',
        "cp": '59000',
        "city": 'Lille'
    },

    "094827": {
        "num_voie": '45',
        "complement": '',
        "voie": 'rue des Arbres',
        "cp": '59510',
        "city": 'Hem'
    }

}

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

            now = datetime.now()
            timecode_for_id = now.strftime("%H%M%S")

            new_num_voie = input("numéro de voie  ? >> ")
            new_complemt = input("complément  ? >> ")
            new_street = input("intitulé de voie  ? >> ")
            new_cp = input("code postal  ? >> ")
            new_city = input("commune  ? >> ")

            new_adress = {
                timecode_for_id: {
                    "num_voie": new_num_voie,
                    "complement": new_complemt,
                    "voie": new_street,
                    "city": new_city,
                    "cp": new_cp,
                }

            }

            data_streets_list.update(new_adress)

        case '2':
            address_id_to_edit = input("quelle adresse voulez-vous éditer => rentrer le numéro ? >> ")
            if address_id_to_edit in data_streets_list:
                
                new_num_voie = input("numéro de voie  ? >> ")
                new_complemt = input("complément  ? >> ")
                new_street = input("intitulé de voie  ? >> ")
                new_cp = input("code postal  ? >> ")
                new_city = input("commune  ? >> ")
                
                # Mettre à jour les champs de l'adresse
                data_streets_list[address_id_to_edit]['num_voie'] = new_num_voie
                data_streets_list[address_id_to_edit]['complement'] = new_complemt
                data_streets_list[address_id_to_edit]['voie'] = new_street
                data_streets_list[address_id_to_edit]['city'] = new_city
                data_streets_list[address_id_to_edit]['cp'] = new_cp
                
            else:
                print(f"Adresse avec l'ID {address_id_to_edit} non trouvée.")

        case '3':
            address_id_to_delete = input("quelle adresse voulez-vous effacer => rentrer le numéro ? >> ")

            if address_id_to_delete in data_streets_list:
                del data_streets_list[address_id_to_delete]
                print(f"Adresse avec l'ID {address_id_to_delete} supprimée.")
            else:
                print(f"Adresse avec l'ID {address_id_to_delete} non trouvée.")

        case '4':
            for key, adress in data_streets_list.items():
                print(f"# => {key}")
                print(f"{adress['num_voie']} {adress['complement']} {adress['voie']}, {adress['cp']} {adress['city']}  \n ------------------------------------------------------------------ ")

        case _:
            break