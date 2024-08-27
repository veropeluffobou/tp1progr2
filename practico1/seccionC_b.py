"""
b. Escribir un programa que resuelva la secuencia de Fibonacci a pedido del usuario. 
Deberá codificar una función fibonacci(numero), cuyo parámetro numero debe ser ingresado 
por el usuario y su tipo, al igual que en el ejercicio anterior, validado. La función debe 
encargarse de calcular la secuencia para dicho número. A continuación, una descripción 
matemática de la famosa secuencia:

"""

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, numero + 1):
            a, b = b, a + b
        return b

# Validar que el dato ingresado sea un dígito
def validar_entrada(entrada):
    return entrada.isdigit()

# Programa principal
numero_ingresado = input("Ingrese un número para calcular la secuencia de Fibonacci: ")

if validar_entrada(numero_ingresado):
    numero = int(numero_ingresado)
    resultado = fibonacci(numero)
    print(f"El número Fibonacci en la posición {numero} es {resultado}.")
else:
    print("Por favor, ingrese un número válido.")


#------------------------------------------------------

def fibonacci_recursiva(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_recursiva(numero - 1) + fibonacci_recursiva(numero - 2)

# Programa principal con función recursiva
numero_ingresado = input("Ingrese un número para calcular la secuencia de Fibonacci: ")

if validar_entrada(numero_ingresado):
    numero = int(numero_ingresado)
    resultado = fibonacci_recursiva(numero)
    print(f"El número Fibonacci en la posición {numero} es {resultado}.")
else:
    print("Por favor, ingrese un número válido.")
