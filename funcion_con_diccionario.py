curso1 = []
curso2 = []
def agregarEstudiante(nombre, edad, calificacion, lista):
    dato = {
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion
    }
    #appen ->> sirve para agregar elementos a una lista
    lista.append(dato)
agregarEstudiante('Ulises', 25, 6, curso1)
agregarEstudiante('Diana', 19, 5, curso1)
agregarEstudiante('Ivan', 25, 7, curso2)

print 'Curso 1:\n', curso1
print '\n'
print 'Curso 2:\n', curso2