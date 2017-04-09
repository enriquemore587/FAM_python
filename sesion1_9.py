'''
1.- programa que lea un numero X

2.- leer un numero y

3.- multiplicar x Y veces

ejemplo:
ingreso:
2

ingreso:
3

programa realiza esto. . .

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
.
.
'''

numeroX = int(raw_input('Ingresa un numero'))

numeroY = int(raw_input('Ingresa un segundo numero'))
# x = 5
# y = 7
contador = 0

while contador < numeroY:
    contador = contador + 1

    cadena = '%d * %d = %d' % (numeroX, contador, numeroX*contador)

    print cadena