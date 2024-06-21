# # # !! ---------- Exercice 1 -------------
# while True:
#     number = int(input("nombre entre 10 et 20 ? >> "))
#     if number >= 10 and number <= 20:
#         print('BRAVO')
#         break
#     elif number > 20:
#         print('TROP GRAND')
#     else:
#         print('TROP PETIT')

# # # !! ---------- Exercice 2 -------------
# number = int(input("nombre ? >> "))
# for i in range(10):
#     number += 1 
#     print(number)

# # # !! ---------- Exercice 3 -------------
# number = int(input("nombre ? >> ")) - 1
# for i in range(10):
#     number += 1 
#     print(number)

# # !! ---------- Exercice 4 -------------
# number = int(input("nombre ? >> "))
# for i in range(1, 11):
#     print(f"{number} X {i} = {number*i} ")

# !! ---------- Exercice 5 -------------
# plus_grand = None

# for i in range(20):
#     number = int(input("nombre ? >> "))
#     if number > plus_grand:
#         plus_grand = number 

# print(plus_grand)

# !! ---------- Exercice 7 -------------
# plus_grand = 0
# position = 0

# for i in range(3):
#     number = int(input("nombre ? >> "))
#     if number > plus_grand:
#         plus_grand = number 
#         position = i+1

# print(f"Le chiffre est {plus_grand} qui se situe à la position {position} ")

# !! ---------- Exercice 8 -------------
# number = abs(int(input("nombre ? >> ")))
# sum = 0

# for i in range(1, number + 1):
#     sum *= i

# print(sum)

# !! ---------- Exercice 9 -------------
# total = 0

# while True:
#     price = int(input("Prix article ? >> "))
#     total += price
#     if price == 0:
#         break
# print(total)

# pay = int(input("Argent donné ? >> "))
# sub = pay - total
# print(f"Monnaie à rendre {sub} Euros")

# if sub // 10 > 0:
#     print(f"Billets 10 : {sub // 10}")
#     # sub -= sub // 10 * 10
#     sub = sub % 10
# if sub // 5 > 0:
#     print(f"Billets 5 : {sub // 5}")
#      # sub -= sub // 5 * 5
#     sub = sub % 5
# if sub > 0:
#     print(f"Pièces de 1 : {sub}")

# !! ---------- Exercice Table de multiplication -------------
# number = int(input("multiplication jusque ? >> "))
# longueur = len(str(number * number))

# for i in range(1, number +1):
    
#     ligne = ""
#     for j in range(1, number +1):
#         space = longueur - len(str(j * i))
#         ligne += str(f"{j * i} {' ' * space}")
#     print(ligne + "\n")

# !! ---------- Pyramide -------------
# height = int(input("hauteur ? >> "))

# for i in range(1, height+1):
#     spaces =  " " * ( height - i )
#     stars = "*" * ( 2 * i - 1 )
#     print(spaces + stars )