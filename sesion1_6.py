#-*- conding:utf-8 -*-

'''
Un programa que lea los datos de un usuario (nombre & la edad)

posteriormente a que los lee.

imprimira la cadena como en el siguiente ejemplo:

Hola 'Enrique' tu edad es: 22

esto si es mayor de edad
'''

nombre = raw_input('EScribe tu nombre: ')

edad = int(raw_input('por favor ingresa tu edad: '))

if edad >= 18:
    print 'ok'