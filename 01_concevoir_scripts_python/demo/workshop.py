#! Calcul  de  la  consommation  énergétique
# conso = input("quelle est votre consommation moyenne par heure ? >> ")
# hours = input("combien d'heures est ouvet votre data center ? >> ")
# conso_totale = int(conso) * int(hours)
# print(f" votre consommation moyenne est estimée à {conso_totale} kW sur votre journée ")

#! calcul Kw / h
# price = input("le coût par kWh ? >> ")
# conso2 = input("quelle est votre consommation moyenne par heure ? >> ")
# hours2 = input("combien d'heures est ouvet votre data center ? >> ")
# conso_totale2 = int(conso2) * int(hours2) * int(price)
# print(f" vous payez environ {conso_totale2} euros pour une journée ")

#! Simulation  de  panne  de  courant
# from datetime import timedelta
# import math

# battery_capacity = input("quelle est la capacité totale des batteries de secours en kW ? >> ")
# conso3 = input("Quelle est la consommation énergétique du data center pour une heure >> ")
# time_remaining = int(battery_capacity) / int(conso3)
# hour_to_seconds = (time_remaining - math.floor(time_remaining)) * 3600
# print(f">> les batteries pourront tenir {math.floor(time_remaining)} heures")

# td = timedelta(seconds=round(hour_to_seconds))

# if hour_to_seconds > 0:
#     print(f">> Il restera {td} avant la coupure définitive")
# else:
#     print('>> Toutes les batteries de secours seront utilisées')

#! L'état du serveur
# isOnMaintenance = input("Le serveur est-il en maintenance ? >> (oui/non) ")
# isOnMaintenance = isOnMaintenance.strip().lower() == 'oui'
# print(f"le serveur est en maintenance : << { bool(isOnMaintenance) } >> ")

#! Bande passante
needs_list = []
needs_to_array_sorted = []
services_ok = []
services_nok = []
bandwidth = int(input("quelle est la bande passante totale disponible dans le data center (en Gbps) ? >> "))

while True:
    bandwidth_by_service = input("1.service : 2.priorité : 3.besoin Gbps ? >> (or 'fin') >> ")
    if bandwidth_by_service == 'fin':

        # Résumé des services déclarés :
        print("######## Vos services déclarés ########")
        bandwidth_total = 0
        for need in needs_to_array_sorted:
            print(f">> {need[0]} : {need[2]}")
            bandwidth_total += int(need[2])
        print("#######################################")
            
        # Calcul de la bande passante :
        if int(bandwidth_total) > bandwidth:
            print(">> WAIT -- Il n'y a pas assez de bande passante dispo, nous devons prioriser ...")
            for need in needs_to_array_sorted:
                
                if bandwidth > 0:

                    # calcul du restant de la bande passante
                    bandwidth -= int(need[2])

                    # dispatch des services OK / NOK
                    if bandwidth > 0:
                        services_ok.append(need[0])
                    else:
                        services_nok.append(need[0])                        
                else:
                    services_nok.append(need[0])
            
            # Affichage final
            print("#######################################")
            print(">> SERVICES OK :")
            for service in services_ok:
                print(f"> {service}")
            print(">> SERVICES NOK :")
            for service in services_nok:
                print(f"> {service}")
            break
        else:
            print(">> SUCCESS -- La bande passante est suffisante pour tous les services déclarés")
            break

    else:
        needs_to_array = bandwidth_by_service.split(" : ")
        needs_to_array_convert = [needs_to_array[0], int(needs_to_array[1]), int(needs_to_array[2])]
        needs_list.append(tuple(needs_to_array_convert))
        needs_to_array_sorted = sorted(needs_list, key=lambda x: (x[1], x[2]))
