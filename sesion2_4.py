# -*- coding: utf-8 -*-
'''
El usuario elija el tamaño
de nuestra matriz
'''

tam = int(raw_input('Ingresa el Tamaño de la matriz: '))

matriz = [ ]

lon_matriz = range(tam)



for filas in lon_matriz:
	
	fila = [ ]

	for columna in lon_matriz:
		if filas == columna:
			fila.append('*')
		else:
			fila.append('1')

	matriz.append(fila)


print '\n'
for fila in matriz:
	print '	', fila

print '\n'