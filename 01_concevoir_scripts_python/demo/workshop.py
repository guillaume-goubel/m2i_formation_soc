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
needs = []
bandwidth = input("quelle est la bande passante totale disponible dans le data center (en Gbps) ? >> ")

while True:
    bandwidth_by_service = input("1.service : 2.priorité du service : 3.besoin bande passante ? >> taper 'fin' pour terminer la liste >> ")
    if bandwidth_by_service == 'fin':

        for need in needs:
            print("######## Vos services déclarés ########")
            print(need)

        break
    else:
 
        foo = bandwidth_by_service.split(" : ")
        needs.append(tuple(foo))
        print(needs)

        toto = sorted(needs, key=lambda priority: priority[1])
        print(toto)

# Pour  chaque  service  (par  exemple,  Web,  Email,  Base  de  données),  demandez  à
# l'utilisateur d'entrer la priorité du service (sur une échelle de 1 à 3, 1 étant le plus haut).
# Demandez ensuite la demande de bande passante pour chaque service (en Gbps).
# En  fonction  de  la  priorité,  allouez  la  bande  passante  disponible  aux  services,  en
# commençant par le service de priorité 1. Si la bande passante totale est insuffisante,
# répartissez-la proportionnellement en fonction de la priorité.
# Affichez la bande passante allouée à chaque service.


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# sorted(student_tuples, key=lambda student: student[2])


