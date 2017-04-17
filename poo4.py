'''
clases  *
atributos   * variables
metodos     * funciones
constructor
def __init__(self, par):
'''
class Robot(object):

    #Atributos
    nombre = None
    color = None

    #Metodos set
    def setNombre(self, nombre):
        self.nombre = nombre
    def setColor(self, color):
        self.color = color

    def mover(self):
        print 'me muevo'

    def saludar(self, persona):
        print 'hola ', persona

if __name__ == '__main__':
    myRobot = Robot()
    myRobot.setNombre('Enrique')
    myRobot.setColor('Verde')
    print myRobot.nombre
    print myRobot.color

    myRobot.mover()
    myRobot.saludar('Juan')
