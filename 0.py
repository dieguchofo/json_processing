# Esto es para ver cómo procesar metadatos.json y plaintext.json

import json
import os

raw = open("plaintext.json")
textos = json.load(raw)

print(type(textos[0][9]))


### SACAR UN TEXTO ###

# primero_s = str(textos[0:5])
# 
# # Escribir 1.txt
# if not os.path.exists('1.txt'):  # Crea 1.txt si no existe
#     os.mknod('1.txt')
# 
# open("1.txt", "w").close()       # borra el contenido de 1.txt
# 
# with open("1.txt", "w") as f:    # llenar "1.txt" con la sopa
#     f.write(primero_s)

### SACAR UN JSON ###
# 
# al_json = textos[0:5]
# 
# # Crea 0.json si no existe
# if not os.path.exists('0.json'):
#     os.mknod('0.json')
# 
# open("0.json", "w").close()     # borra el contenido de 0.json
# 
# with open('0.json', 'a') as f:  # escribe el .json
#         json.dump(al_json, f)
#         f.write('\n')