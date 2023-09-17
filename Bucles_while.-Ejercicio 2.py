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


"""Ejercicio 2.
Genere un diccionario vacío que luego se irá llenando según lo que ingrese el
usuario. Pedir los siguientes datos:
ISBN
Nombre del libro
Stock
Precio del libro
Cuando el usuario ingrese un 0 como ISBN se deberá imprimir:
Todos los datos ingresados
La cantidad total de libros
El monto total de todos los libros
El valor promedio de los libros """


# Inicializamos un diccionario vacío para almacenar los datos de los libros
libros = {}

while True:
    isbn = input("Ingrese el ISBN del libro (0 para terminar): ")

    # Si el usuario ingresa '0' como ISBN, salimos del bucle
    if isbn == '0':
        break

    nombre = input("Ingrese el nombre del libro: ")
    stock = int(input("Ingrese el stock del libro: "))
    precio = float(input("Ingrese el precio del libro: "))

    # Creamos un diccionario con la información del libro
    libro = {
        'ISBN': isbn,
        'Nombre': nombre,
        'Stock': stock,
        'Precio': precio
    }

    # Agregamos el libro al diccionario de libros
    libros[isbn] = libro

# Imprimimos todos los datos ingresados
print("\nDatos de los libros ingresados:")
for isbn, libro in libros.items():
    print(f"ISBN: {libro['ISBN']}")
    print(f"Nombre del libro: {libro['Nombre']}")
    print(f"Stock: {libro['Stock']}")
    print(f"Precio del libro: {libro['Precio']}")
    print()

# Calculamos la cantidad total de libros
cantidad_total = sum(libro['Stock'] for libro in libros.values())

# Calculamos el monto total de todos los libros
monto_total = sum(libro['Stock'] * libro['Precio'] for libro in libros.values())

# Calculamos el valor promedio de los libros
valor_promedio = monto_total / cantidad_total

# Imprimimos los resultados
print(f"Cantidad total de libros: {cantidad_total}")
print(f"Monto total de todos los libros: {monto_total}")
print(f"Valor promedio de los libros: {valor_promedio:.2f}")
