#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      anale
#
# Created:     27/08/2023
# Copyright:   (c) anale 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Ejercio 2
# Pedir al usuario que ingrese dos nros
# Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
# Pedir al usuario que ingrese una opción
# Verificar la opción del usuario
# Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
# ingrese una opción
# Ejecutar la operación
# Mostrar por pantalla el resultado


# Pedir al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Mostrar las opciones disponibles
print("Opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

# Iniciar un bucle que se ejecutará hasta que el usuario ingrese una opción válida
while True:
    opcion = int(input("Ingrese una opción (1/2/3): "))

    # Verificar si la opción ingresada es válida
    if opcion in [1, 2, 3]:
        if opcion == 1:
            resultado = num1 + num2
        elif opcion == 2:
            resultado = num1 - num2
        else:
            resultado = num1 * num2
        # Mostrar el resultado de la operación y salir del bucle
        print("Resultado:", resultado)
        break
    else:
        # Mostrar un mensaje de error si la opción no es válida
        print("Opción incorrecta. Intente nuevamente.")


