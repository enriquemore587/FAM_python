import matplotlib.pyplot as plt
def cubo(numero):
    ejeX = range(numero)
    # x = [0, 1, 2]
    ejeY = []
    # y = []
    for elemento in ejeX: # 0, 1, 2
        ejeY.append(elemento**3) # y = [0,1, 4]
    # x = [0, 1, 2]
    # y = [0, 1, 4]
    diccionario = {
        'ejeX': ejeX,
        'ejeY': ejeY
    }
    '''
    diccionario = {
        'ejeX': [0,1,2],
        'ejeY': [0,1,4]
    }
    '''
    return  diccionario
def cuadrado(numero):
    ejeX = range(numero)
    # x = [0, 1, 2]
    ejeY = []
    # y = []
    for elemento in ejeX: # 0, 1, 2
        ejeY.append(elemento**2) # y = [0,1, 4]
    # x = [0, 1, 2]
    # y = [0, 1, 4]
    diccionario = {
        'ejeX': ejeX,
        'ejeY': ejeY
    }
    '''
    diccionario = {
        'ejeX': [0,1,2],
        'ejeY': [0,1,4]
    }
    '''
    return  diccionario
def plotear(numero):
    datos_graficar = cuadrado(numero)
    print datos_graficar['ejeX']
    print datos_graficar['ejeY']
    plt.plot(datos_graficar['ejeX'], datos_graficar['ejeY'], '-')
    plt.show()

def plotear_delegamiento(numero, funcion_plotear):
    datos_graficar = funcion_plotear(numero)
    plt.plot(datos_graficar['ejeX'], datos_graficar['ejeY'], '-')
    plt.show()

plotear_delegamiento(8, cuadrado)