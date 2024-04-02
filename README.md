Esto es un pequeño proyecto para tener finalmente un json con el cual trabajar.
Creo que no me importa que sea human-readable, entonces chance dejo todo en
una sola línea. Quiero:
    [LOGRADO] 1. Testear que sea computer-readable (Poder accesar cada página
    de cada archivo)
    2. Tener un json que tenga doc_num, año, título y texto

Mis textos sagrados son metadatos.json y plaintext.json

Creo que tengo que descartar "0345656_A1.pdf". El texto es ininteligible

### DESCIFRANDO LA ESCTRUCTURA DE PLAINTEXT.JSON ###

[[{TEXTO 1 PAG 1}, {TEXTO 1 PAG 2}, {ETC.}, 
{TEXTO 2 PAG 1}, {TEXTO 2 PAG 2}, {ETC.}]]


La jerarquía va, de más grande a más pequeño:
list,
    list,
        dict

Todo es una gran lista (bien)
Cada elemento de esa lista es otra lista, que corresponde a un trabajo de 
titulación (mal)
Cada elemento de _esa_ lista es un diccionario, que tiene "doc_num" y "texto"
(mal)

Esto resulta en que cada trabajo de titulación esté almacenado con cada página
separada (bien) y con su doc_num anexado (mal). Se ve así:
    [
        [
            {"doc_num": "x", "texto": "PAG_1"}, {"doc_num": "x", "texto": "PAG_2"},
            {ETC.}
        ],
        [
            {"doc_num": "y", "texto": "PAG_1"}, {"doc_num": "y", "texto": "PAG_2"},
            {ETC.}
        ],
        [ETC.]
    ]

Lo que debe ser es que todo sea una gran lista (listo), y que cada elemento de
esa lista corresponda a un trabajo de titulación pero como un diccionario
(falta), que sea así:
    {"doc_num": "x",
    "texto": ["PAG_1", "PAG_2", "ETC."]}

En total debería verse así:
    [
        {"doc_num": "1 (por decir)",
        "texto": ["PAG_1", "PAG_2", "ETC."]},
        {"doc_num": "2",
        "texto": ["PAG_1", "PAG_2", "ETC."]},
        {ETC.}
    ]

Lógicamente, debería hacer esto:
    - por cada elemento de la lista grandota:
        - extraer el doc_num del primer elemento (el primer diccionario). Esto lo hace 0.0.py
        - appendear a una lista el "texto" de cada diccionario            Esto lo hace 0.1.py
        - juntar los códigos para que quede la lista bonita
    - ordenar eso (NO SÉ CÓMO TODAVÍA)