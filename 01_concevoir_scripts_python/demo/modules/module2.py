from module1 import saluer, addition, pi
import os
import utils

print(saluer('toto'))

file_name = 'file_for_module.txt'

def add_lign_in_file(lign):
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(lign)
    else:
        with open(file_name, 'w+') as file:
            file.write(lign)

