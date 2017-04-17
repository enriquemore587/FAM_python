#!/usr/bin/python
# -*- coding: utf-8 -*-


import smtplib


def enviar(nombre, destinatario):
    msg = '''
    Hola %s''' % nombre

    # Datos
    username = 'jose.vergara2104@gmail.com'
    password = 'slqiqlkgyeifcora'

    # Enviando el correo
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(username, destinatario, msg)
    server.quit()

#from lib_FAM import load_xl, data_map

##          En esta parte cargamos los datos de EXCEL
#datos = load_xl('Acreedores a Curso TESE ISC-2017.xlsx', 'Sheet1', 'C5:D19')

def nombre(dic):
    return (dic['Nombre'],dic['Correo'])

#datos = data_map(datos, nombre)
#enviar('enrique', 'ureyesz@outlook.com')
#enviar(nombre.encode('utf-8'), correo.encode('utf-8'))