import csv

doc = open('archivo.csv', 'w')

doc_csv_w = csv.writer(doc)

lista = ['Enrique', 9999]

doc_csv_w.writerow(lista)

doc.close()