tam = int(raw_input('Ingresa el Tamaño de la matriz: '))

matriz = [ ]

lon_matriz = range(tam)

indicador = 1

for filas in lon_matriz:
	
	fila = [ ]

	for columna in lon_matriz:
		fila.append(indicador)
		indicador = indicador + 1
		
	matriz.append(fila)


print '\n'
for fila in matriz:
	print '	', fila