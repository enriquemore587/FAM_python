from random import choice, randint

def fecha():
    meses = ["1", "2", "3"]
    
    dia = randint(1, 28)
    mes = choice(meses)
    aa = choice([2014, 2015, 2016])

    return "%d-%s-%d" %(dia, mes, aa)

nombres = ["Enrique", "Mariana", "Ulises", "Ivan"]

clientes = []

for i in range(1000):
    cliente = {
        "Nombre": choice(nombres),
        "Fecha": fecha(),
        "Consumo": randint(10, 1000)
    }

    clientes.append(cliente)

import lib_FAM as lib

lib.write_xl("clientes2.xlsx", "Hoja1", "A1",
    clientes, ["Consumo", "Nombre", "Fecha"])
