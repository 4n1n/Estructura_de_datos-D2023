#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      anale
#
# Created:     17/09/2023
# Copyright:   (c) anale 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""Ejercicio 1.
Genere una lista vacía que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
Nombre de sucursal
Nombre de sucursal
Cantidad de ventas
Venta total de la sucursal
Se deberá sacar el promedio de ventas en pesos de esa sucursal
Cuando el usuario ingrese un 0 como nombre de sucursal se deberá imprimir:
Todos los datos ingresados
El promedio de cada sucursal
El total vendido por toda la cadena
"""

# Crear una lista vacía para almacenar la información de las sucursales
sucursales = []

while True:
    # Pedir al usuario el nombre de la sucursal
    nombre_sucursal = input("Ingrese el nombre de la sucursal (0 para salir): ")

    # Verificar si el usuario quiere salir del programa
    if nombre_sucursal == '0':
        break

    # Pedir la cantidad de ventas y la venta total de la sucursal
    cantidad_ventas = int(input("Ingrese la cantidad de ventas: "))
    venta_total = float(input("Ingrese la venta total de la sucursal en pesos: "))

    # Calcular el promedio de ventas de la sucursal
    promedio_ventas = venta_total / cantidad_ventas

    # Crear un diccionario con la información de la sucursal
    sucursal = {
        'Nombre': nombre_sucursal,
        'Cantidad de Ventas': cantidad_ventas,
        'Venta Total': venta_total,
        'Promedio de Ventas': promedio_ventas
    }

    # Agregar el diccionario a la lista de sucursales
    sucursales.append(sucursal)

# Imprimir todos los datos ingresados
print("Datos ingresados:")
for sucursal in sucursales:
    print(f"Sucursal: {sucursal['Nombre']}")
    print(f"Cantidad de Ventas: {sucursal['Cantidad de Ventas']}")
    print(f"Venta Total: {sucursal['Venta Total']} pesos")
    print(f"Promedio de Ventas: {sucursal['Promedio de Ventas']} pesos por venta")
    print()

# Calcular el total vendido por toda la cadena
total_vendido_cadena = sum(sucursal['Venta Total'] for sucursal in sucursales)
print(f"Total vendido por toda la cadena: {total_vendido_cadena} pesos")

