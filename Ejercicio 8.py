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
#Ejercicio 8

lista = [10, 5, 8, 20, 3]
min_valor = lista[0]
for num in lista:
    if num < min_valor:
        min_valor = num
print("Valor mínimo:", min_valor)
