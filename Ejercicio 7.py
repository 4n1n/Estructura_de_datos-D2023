#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anale
#
# Created:     27/08/2023
# Copyright:   (c) anale 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Ejercicio 7


lista = [10, 5, 8, 20, 3]
max_valor = lista[0]
for num in lista:
    if num > max_valor:
        max_valor = num
print("Valor máximo:", max_valor)

