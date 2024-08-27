"""
c. Escriba un procedimiento procesar_palabras(entrada) que acepte una secuencia de palabras separadas 
por coma, las ordene y las imprima. Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te
"""

def procesar_palabras(entrada):
    palabras = entrada.split(',')  # Separar las palabras usando la coma como delimitador
    palabras_ordenadas = sorted(palabras)  # Ordenar las palabras alfabéticamente
    resultado = ','.join(palabras_ordenadas)  # Unir las palabras ordenadas con comas
    print(resultado)  # Imprimir el resultado

# Ejemplo de uso:
entrada = "te,felicito,que,bien,actuas"
procesar_palabras(entrada)  # Esto imprimirá: actuas,bien,felicito,que,te
