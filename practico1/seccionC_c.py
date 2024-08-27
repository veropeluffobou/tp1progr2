"""
c. Tal como sucede con la lógica proposicional, en Python muchas veces las expresiones booleanas 
pueden ser simplificadas manteniendo el valor de verdad de la expresión. Así, por ejemplo, 
(a and b) or (b and a) es equivalente a a and b. A continuación, intente simplificar las siguientes 
expresiones y escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el valor de 
verdad de las expresiones ya simplificadas:
i. (a or b) or (b and c)
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False
"""

def procesar_sentencias(a, b, c):
    # Simplificación i: (a or b) or (b and c) -> a or b
    resultado_i = a or b
    
    # Simplificación ii: b and c or False -> b and c
    resultado_ii = b and c
    
    # Simplificación iii: a and b or c or (b and a) -> a and b or c
    resultado_iii = a and b or c
    
    # Simplificación iv: a == True or b == False -> a or not b
    resultado_iv = a or not b
    
    return resultado_i, resultado_ii, resultado_iii, resultado_iv

# Prueba del procedimiento con valores de ejemplo
a = True
b = False
c = True

resultados = procesar_sentencias(a, b, c)
print("Resultados de las expresiones simplificadas:")
print(f"Expresión i: {resultados[0]}")
print(f"Expresión ii: {resultados[1]}")
print(f"Expresión iii: {resultados[2]}")
print(f"Expresión iv: {resultados[3]}")

