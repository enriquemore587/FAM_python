import csv

doc = open('archivo.csv', 'w')

doc_csv_w = csv.writer(doc)

lista = [['Enrique', 9999], ['Mariana', 2299], ['Luis', 9933]]

doc_csv_w.writerows(lista)

doc.close()