#!/usr/bin/python
# -*- coding: utf-8 -*-

# importamos el modulo socket
import socket


# instanciamos un objeto para trabajar con el socket
puerto = int(raw_input('Escribe el puerto en el que vas a crear tu SERVIDOR '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# con el metodo bind indicamos que puerto vamos a ocupar
# el primer argumento es un string e indiga el cliente que va a aceptar
# si lo dejamos en blanco aceptara a cualquiera.

print '-*' * 200

print 'Se esta Creando el Servidor'
s.bind(("", puerto))


#   aceptamos conexiones entrantes externas y aperte indicamos cuantas
s.listen(1)

print 'El servidor se Creo Satisfactoria mente'
#   el servidor se queda escuchando el puerto

print '\n \n -----  se esta esperando a que se conecte el cliente'
socketCliente, addr = s.accept() # (name, 192.0.0.1)

print '\n' * 10

print 'se conecto: ', addr

#   el servidor ya recibio al cliente.
#   recuperamos la conexion & la direccion ip

# cerramos el socket del servidor
s.close()
print 'Cerramos el Socket Servidor'