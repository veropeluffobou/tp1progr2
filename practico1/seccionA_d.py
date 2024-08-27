"""
Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) 
que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']
"""

def listas_diferencia(lista1, lista2):
    # Convertimos las listas en conjuntos para realizar operaciones de conjuntos
    set1 = set(lista1)
    set2 = set(lista2)

    # Encontramos los elementos en común (intersección) y los ordenamos en orden inverso
    comunes = sorted(set1.intersection(set2), reverse=True)

    # Encontramos los elementos no comunes (diferencia simétrica) y los ordenamos alfabéticamente
    no_comunes = sorted(set1.symmetric_difference(set2))

    # Imprimimos los resultados
    print(comunes)
    print(no_comunes)

# Ejemplo de uso:
lista1 = ['b', 'a', 'c']
lista2 = ['e', 'b', 'd', 'c']
listas_diferencia(lista1, lista2)

