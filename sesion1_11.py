archivo = open('ejemplo.txt', 'w')

numeroX = int(raw_input('Ingresa un numero'))

numeroY = int(raw_input('Ingresa un segundo numero'))

contador = 0

cadenaFinal = ''

while contador < numeroY:
    contador = contador + 1
    cadena = '%d * %d = %d\n' % (numeroX, contador, numeroX * contador)
    cadenaFinal = cadenaFinal + cadena
archivo.write(cadenaFinal)
archivo.close()