#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      anale
#
# Created:     27/08/2023
# Copyright:   (c) anale 2023
# Licence:     <your licence>
#----------------------------------------------------------------------------
# Ejercicio 1
# Pedir al usuario que ingrese un nro impar
# Mientras que el usuario no ingrese un nro impar se volverá a pedir que ingrese
# un nro impar
# Deberá indicar por pantalla si es impar

while True:
    num = int(input("Ingrese un número impar: "))
    if num % 2 != 0:
        print("Es un número impar.")
        break
    else:
        print("No es un número impar. Intente nuevamente.")
