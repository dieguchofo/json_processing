# Esto pretende hace una lista de listas, cuyos elementos son las páginas
# de los trabajos de titulación. Se ve así:
# [
#   ["PAG_1", "PAG_2", ETC.],
#   ["PAG_1", "PAG_2", ETC.],
#   ETC.
# ]
import json
import os

raw = open("plaintext.json")
textos = json.load(raw)

c_1 = len(textos) - 1    # c_1 para el loop mayor, de la lista grandota
c_1_0 = 0
lista= []

# c_1 es la cantidad de trabajos. Empieza siendo 492
# c_1_0 empieza siendo 0 y eventualmente llega a ser uno más que c_1
# c_2 es la cantidad de paginas en cada trabajo
# c_2_0 empieza siendo 0 y eventualmente llega a ser uno más que c_2

while c_1 >= 0:
    c_2 = len(textos[c_1_0]) - 1
    c_2_0 = 0

    while c_2_0 <= c_2:
        lista.append([])
        print(c_1_0, c_2_0, c_2)
        lista[c_1_0].append(textos[c_1_0][c_2_0]["texto"])

        c_2_0 = c_2_0 + 1

    c_1 = c_1 - 1
    c_1_0 = c_1_0 + 1

print(lista[273][2])