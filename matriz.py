# -*- coding: utf-8 -*-

'''
matriz = []
filas = raw_input('FILAS:_')
columnas = raw_input('COLUMNAS:_')
contador = 0
for i in range(int(filas)):
	fila = []
	for j in range(int(columnas)):
		fila.append(contador)
		contador = contador + 1
	matriz.append(fila)


for i in matriz:
	print i
'''

'''
matriz = []

tam = int(raw_input('Tamaño de la matriz:_'))

for x in range(1, tam+1):
	fila = [ ]
	for y in range(1, tam+1):
		if x == y:
			fila.append('*')
		else:
			fila.append('%d,%d' %(x,y))
	matriz.append(fila)

for x in matriz:
	print x
'''
'''
matriz = []

tam = int(raw_input('Tamaño de la matriz:_'))

indicador = tam - 1
for x in range(1, tam):
	fila = [ ]
	for y in range(1, tam):
		if indicador == y:
			fila.append('*')
			indicador -= 1
		else:
			fila.append('%d,%d' %(x,y))
	matriz.append(fila)

for x in matriz:
	print x
'''

matriz = []

tam = int(raw_input('Tamaño de la matriz:_'))

indicador = 1

for x in range(1, tam+1):
	fila = [ ]
	for y in range(1, tam+1):
		fila.append(int(indicador))
		indicador += 1
	matriz.append(fila.sort(reverse=True) )


print '\n'

for x in matriz:
	print '	' + (str(x))
	print '\n'