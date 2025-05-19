# 22) Se tienen tres baldes de agua, uno de cinco litros, otro de tres litros y otro de un litro; si el de un litro tarda una hora y media en llenarse, resuelva cuánto tiempo pueden tardar en llenarse los otros baldes.
# Si tiene tres baldes, pero se desconoce su tamaño debe de resolver igualmente el ejercicio.

def tiempo_llenado(capacidad_balde, tiempo_balde_un_litro=1.5):
    """
    Calcula el tiempo necesario para llenar un balde de agua en función de su capacidad.
    :param capacidad_balde: Capacidad del balde en litros.
    :param tiempo_balde_un_litro: Tiempo que tarda en llenarse un balde de 1 litro (en horas).
    :return: Tiempo necesario para llenar el balde (en horas y minutos).
    """
    tiempo_total_horas = capacidad_balde * tiempo_balde_un_litro
    horas = int(tiempo_total_horas)
    minutos = int((tiempo_total_horas - horas) * 60)
    return horas, minutos

# Baldes conocidos
baldes = [5, 3, 1]

print("Tiempos de llenado para baldes conocidos:")
for balde in baldes:
    horas, minutos = tiempo_llenado(balde)
    print(f"Balde de {balde} litros: {horas} horas y {minutos} minutos")

# Caso general: tamaños desconocidos
print("\nTiempos de llenado para baldes de tamaños desconocidos:")
tamaños_desconocidos = [7, 2, 4]  # Ejemplo de tamaños desconocidos
for balde in tamaños_desconocidos:
    horas, minutos = tiempo_llenado(balde)
    print(f"Balde de {balde} litros: {horas} horas y {minutos} minutos")