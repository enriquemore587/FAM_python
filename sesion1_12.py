archivo = open('doc.mp3', 'a')
contador = 1
while True:
    contador = contador + 1
    archivo.write(str(contador * contador))

archivo.close()