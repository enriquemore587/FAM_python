import csv

doc = open('archivo.csv', 'r')

doc_csv = csv.reader(doc)

for (nombre, numero) in doc_csv:
	print nombre, numero

doc.close()