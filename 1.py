# esto junta 0.0.py y 0.1.py
# tiene como input plaintext.json y lo reordena para que quede bonito:
#     [
#         {"doc_num": "1 (por decir)",
#         "texto": ["PAG_1", "PAG_2", "ETC."]},
#         {"doc_num": "2",
#         "texto": ["PAG_1", "PAG_2", "ETC."]},
#         {ETC.}
#     ]

# También junta los plaintexts con sus respectivos metadatos.
# El archivo se divide en dos: 
#   - reordenar plaintext.json y
#   - juntar con los metadatos

import json
import os

###############################################################################
######################## REORDENAR PLAINTEXT.JSON #############################
###############################################################################

raw = open("plaintext.json")
textos = json.load(raw)

### EXTRAE DOC_NUMS ###

doc_nums = []

contador_1 = len(textos) - 1    # para el loop mayor, de la lista grandota
contador_0 = 0

while contador_1 >= 0:
    doc_nums.append(textos[contador_1][0]["doc_num"])
    contador_1 = contador_1 - 1
    #print(contador_1)

#print(doc_nums)

### EXTRAE EL TEXTO ###

c_1 = len(textos) - 1    # c_1 para el loop mayor, de la lista grandota
c_1_0 = 0
texto = []

# c_1 es la cantidad de trabajos. Empieza siendo 492
# c_1_0 empieza siendo 0 y eventualmente llega a ser uno más que c_1
# c_2 es la cantidad de paginas en cada trabajo
# c_2_0 empieza siendo 0 y eventualmente llega a ser uno más que c_2

while c_1 >= 0:
    c_2 = len(textos[c_1_0]) - 1
    c_2_0 = 0

    while c_2_0 <= c_2:
        texto.append([])
        #print(c_1_0, c_2_0, c_2)
        texto[c_1_0].append(textos[c_1_0][c_2_0]["texto"])

        c_2_0 = c_2_0 + 1

    c_1 = c_1 - 1
    c_1_0 = c_1_0 + 1

#print(texto[273])

### JUNTA DOC_NUMS Y TEXTO EN UNA LISTA DE DICCIONARIOS ###

doc_nums.reverse()  # inicialmente, los doc_nums estaban del más chico al más grande y los trabajos de titulación estaban en el orden inverso

todo = []

c1 = len(doc_nums) - 1
c10 = 0
while c10 <= c1:
    dicc = {"doc_num": doc_nums[c10], "texto": texto[c10]}
    todo.append(dicc)
    c10 = c10 + 1

###############################################################################
######################### JUNTAR CON LOS METADATOS ############################
###############################################################################

raw.m = open("metadatos.json")
metadatos = json.load(raw.m)

### prueba ###

prueba = metadatos[0:4]