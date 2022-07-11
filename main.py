import perceptron

def entrenamiento():
    archivo = open('iris_train.data')   #archivo de entrenamiento

    #lee el archivo y lo guarda en una lista
    datos = []
    for linea in archivo:
        dato = linea.split(',')
        datos.append(dato)

    #Cambia iris setosa por 1
    for i in range(len(datos)):
        if datos[i][4] == 'Iris-setosa\n':
            datos[i][4] = 1
        else:
            datos[i][4] = -1

    #introducir los datos al perceptron
    for i in range(len(datos)):
        perceptron.intorduce_datos(datos[i])

    #Se entrena el perceptron
    perceptron.entrenamiento()


#Se hace la prueba
def prueba():
    archivo = open('iris_validation.data')  #archivo de prueba
    for linea in archivo:
        dato = linea.split(',')
        print('Dato a validar: ',dato)
        valor = perceptron.prueba(dato)
        if valor == 1:
            print('Iris-setosa')
        else:
            print('Iris-versicolor')
        print('\n')

entrenamiento()
prueba()