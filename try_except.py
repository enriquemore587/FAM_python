'''
dato = raw_input('ingresa un Numero:  ')

try:
    print int(dato) / 2
except:
    print 'Oye amigo %s no es un numero' % (dato)
'''
dato = raw_input('ingresa un Numero:  ')

try:
    try:
        dato = int(dato)
    except:
        print 'No se puede Convertir a entero'
    dato = dato / 2
except:
    print 'Oye amigo %s no es un numero' % (dato)
print dato