contador = 0
archivo1 = open('Pares.txt', 'a')
archivo2 = open('Impares.txt', 'a')
while True:
    if contador == 100:
        break
    contador = contador + 1
    resultado = contador % 2
    if resultado == 0:
        archivo1.write(str(contador)+'\n')
        continue
    archivo2.write(str(contador)+'\n')

archivo1.close()
archivo2.close()