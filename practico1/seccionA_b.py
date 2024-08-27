"""
b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y cuando las letras 
que componen dicha palabra estén en orden alfabético, y False en caso contrario.
"""
def es_abc(palabra):
    palabra = palabra.lower()  # Convertimos a minúsculas para evitar problemas con mayúsculas
    return list(palabra) == sorted(palabra)

# Ejemplos de uso:
print(es_abc("abc"))       # True, las letras están en orden alfabético
print(es_abc("ace"))       # True, las letras están en orden alfabético
print(es_abc("cba"))       # False, las letras no están en orden alfabético
print(es_abc("abz"))       # True, las letras están en orden alfabético
print(es_abc("apple"))     # False, porque "p" viene antes que "l"

