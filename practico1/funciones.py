import time

# Calcular si es un año bisiesto
def anio_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Calcular el número de días de cada mes
def calcular_dias_mes(mes, es_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto else 28

# Validar que la edad ingresada es numérica
def validar_edad(edad):
    return edad.isdigit()

# Calcular la edad en días
def calcular_dias_edad(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        dias += 366 if anio_bisiesto(a) else 365

    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

    dias += hora_local.tm_mday
    return dias
