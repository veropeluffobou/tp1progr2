"""
a. Escribir una función de nombre palabra_no_tiene_letras(palabra, letras_prohibidas), 
la cual retorne True si es que los caracteres que componen una palabra no se encuentran 
en una lista de caracteres prohibidos.
"""
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

palabra = "programacion"
letras_prohibidas = ['a', 'i']

resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
print(resultado)  # Esto imprimirá False porque "a" e "i" están en la palabra

palabra = "programacion"
letras_prohibidas = ['j', 'k']

resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
print(resultado)  # Esto imprimirá True porque "j" e "k" no están en la palabra

