'''
key, valor
'identificador': <int, float, boolean, str>
'''

diccionario = {
    'nombre': 'Jose Enrique',
    'edad': 35,
    'estatura': 1.72,
    'nacionalidad': 'Mexicano',
    'prestado': ['raspberry', 'laptop', 'teclado'],
    'status': True,
    'hijos': {
        'nombre': 'Jr',
        'edad': 5
    }
}
arreglo = [
    1,
    'string',
    ['1',2,3],
    diccionario
]
variable = arreglo[3]

variable_edad = variable["edad"]


for elemento in variable:
    print variable_edad