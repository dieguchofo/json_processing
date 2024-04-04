# esto es pa sacar el año de publicación y el título

import json
import os

raw = open("metadatos.json")
metadatos = json.load(raw)

### AÑOS DE PUBLICACIÓN ###

anos = []

contador_1 = len(metadatos) - 1
contador_0 = 0

while contador_1 >= 0:
    anos.append(metadatos[contador_1]["año"])
    contador_1 = contador_1 - 1
    print(contador_1)

print(len(anos))