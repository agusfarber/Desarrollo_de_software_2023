"""
Funciones para operar sobre una lista
Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

1) Muestre la lista

2) El usuario debe ingresar un valor. El programa debe informar cuántos valores de la 
lista son mayores a dicho valor, para eso debe utilizar una función. La función debe recibir como 
argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.

3) Crear una función que calcule el promedio de la lista y utilizarla.

4) Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.
"""

lista = []

import random

def cargar():
    for i in range (10):
        numero = random.randint(1,20)
        lista.append(numero)

def mostrar():
    #1
    print(f"La lista es: {lista}")

def calcularMayores(valor):
    contador = 0
    for elem in lista:
        if elem > valor:
            contador = contador + 1
    return contador

def calcularPromedio():
    suma = 0
    for elem in lista:
        suma = suma + elem
    promedio = suma / 10
    return promedio

def calcularMayorMenor():
    mayor = 0
    menor = 21
    for elem in lista:
        if elem > mayor:
            mayor = elem
    for elem in lista:
        if elem < menor:
            menor = elem
    return (mayor, menor)


cargar()
mostrar()

valor = int(input("Ingrese un valor: "))

cantidadMayores = calcularMayores(valor)

#2
print(f"La cantidad de valores en la lista mayores al valor ingresado es: {cantidadMayores}")

promedio = calcularPromedio()

#3
print(f"El promedio de los elementos de la lista es: {promedio}")

(mayor, menor) = calcularMayorMenor()

#4
print(f"El Mayor es: {mayor}, y el Menor es: {menor}")