#!/usr/bin/python
# -*- coding: utf-8 -*-

#   importamos al modulo socket
import socket

#   hacemos una instancia de un socket
s = socket.socket()
#   importamos el modulo time
import time

#valor1, valor2 = 10, 15
server, puerto = str(raw_input('ip del server: ')), int(raw_input('Puerto a Conectar'))
#   con el socket ya creado nos conectamos al
#   servidor

print '''Se esta conectando al servidor: %s
            -   Al puerto: %d''' % (server, puerto)
time.sleep(1)

s.connect((server, puerto))

print ''' Conexion establecida. . .'''

while True:
    print '''\n
    1.- Mandar correo
    2.- Consultar B.D.
    3.- Salir
    '''
    msj = raw_input('Elige una opcion: ') # 1, 2, 3

    if msj == '3':
        s.send('3')
        break
    elif msj == '1':

        correo = raw_input('Escribe tu correo: ')
        contenido = raw_input('Escribe el contenido: ')
        msj = '%s,%s' % (msj, '%s*%s' % (contenido,correo))
        s.send(msj)
    elif msj == '2':
        peticion = 'Ver la Base de Datos'
        msj = '%s,%s' % (msj, peticion)
        s.send(msj)
    print 'Solicitud Enviada. . . \n'
    time.sleep(1)
    respServer = s.recv(1024)


    print 'Servidor contesto: %s' % respServer

s.close()