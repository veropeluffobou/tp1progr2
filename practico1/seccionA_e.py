"""
e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de números, 
eleve cada elemento impar en ella al cuadrado y los mueva a otra lista e imprima ambas. 
La lista de números la ingresa el usuario en forma de números separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81
"""

def numeros_par_impar(entrada):
    # Convertimos la entrada en una lista de números
    numeros = [int(x) for x in entrada.split(',')]

    pares = []
    impares_cuadrados = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares_cuadrados.append(numero ** 2)

    # Convertimos las listas a cadenas de texto separadas por comas y las imprimimos
    print("Números pares")
    print(','.join(map(str, pares)))
    print("Números impares elevados al cuadrado")
    print(','.join(map(str, impares_cuadrados)))

# Ejemplo de uso:
entrada = "1,2,3,4,5,6,7,8,9"
numeros_par_impar(entrada)
