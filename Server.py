#!/usr/bin/python
# -*- coding: utf-8 -*-

# importamos el modulo socket
import socket

def createServer():
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
    socketCliente, addr = s.accept()  # (name, 192.0.0.1)

    print '\n' * 10

    print 'se conecto: ', addr

    while True:
        # el servidor recibe una peticion
        msj = socketCliente.recv(1024)
        cadena = msj.split(',')#[1,msg*ureyesz@outlook.com]
        print '%s Correo: %s' % ( str(addr) , cadena[1])

        if msj == '3':
            print 'Conexion Terminada'
            break
        elif cadena[0] == '1':#el indicador  uno es mandar correo
            import correo
            try:
                datos = (cadena[1]).split('*')
                correo.enviar(datos[0], datos[1])
            except:
                print 'no se pudo mandar el correo'
            print 'enviara un correo'
            msj = 'El correo electronico se enviara'
        elif cadena[0] == '2':#el indicador  uno es mandar conectar a la b.d
            print 'consultar la B.D'
            msj = 'Se consultara la Base de datos'
        socketCliente.send(msj)

    socketCliente.close()
    s.close()




if __name__ == '__main__':
    createServer()