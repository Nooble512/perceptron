import random

pesos = []
datos = []

#los datos son una lista de 4 elementos que son los atributos y 1 elemento que es el resultado
def intorduce_datos(data):
    datos.append(data)
    pesos.clear()
    nuevos_pesos()

#genera un peso aleatorio para cada atributo entre el 0 y 1
def nuevos_pesos():
    for i in range(len(datos[0])-1):
        pesos.append(random.uniform(0,1))

#suma los pesos con los datos
def suma(dato):
    suma = 0
    for i in range(len(dato)-1):
        suma += pesos[i] * float(dato[i])
    return suma

#si la suma es mayor que 0, se activa, si no, no se activa
def activacion(suma):
    if suma > 0:
        return 1
    else:
        return -1

#entrena el perceptron
def entrenamiento():
    contador = 0
    while contador < len(datos):
        sum = suma(datos[contador])
        activation = activacion(sum)
        error = datos[contador][len(datos[contador])-1] - activation
        if error == 0: #si el error es 0, no hay error, no se actualiza el peso
            contador += 1
        else:
            for i in range(len(datos[contador])-1):
                pesos[i] += error * float(datos[contador][i]) * random.uniform(0,1)
            contador = 0

#prueba el perceptron
def prueba(dato):
    sum = suma(dato)
    activation = activacion(sum)
    return activation
