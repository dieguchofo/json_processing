# Esto va a: 
#   - por cada elemento de la lista grandota:
#       - extraer el doc_num del primer elemento (el primer diccionario).
#       - appendear a una lista el "texto" de cada diccionario
# Ya logra extraer el doc_num de cada elemento

import json
import os

raw = open("plaintext.json")
textos = json.load(raw)

doc_nums = []

contador_1 = len(textos) - 1    # para el loop mayor, de la lista grandota
contador_0 = 0

while contador_1 >= 0:
    doc_nums.append(textos[contador_1][0]["doc_num"])
    contador_1 = contador_1 - 1
    print(contador_1)

print(doc_nums)