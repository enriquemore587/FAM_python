numeroX = int(raw_input('Ingresa un numero'))

numeroY = int(raw_input('Ingresa un segundo numero'))
# x = 5
# y = 7
contador = 0
archivo = open('choster.txt', 'a')
while contador < numeroY:
    contador = contador + 1

    cadena = '%d * %d = %d' % (numeroX, contador, numeroX*contador)
    print cadena
    archivo.write(cadena)
    archivo.write('\n')


archivo.write('\n\n')
archivo.close()
print 'archivo modificado'