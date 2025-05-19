# 23) Una persona tarda 5 horas en subir una montaña de 7 metros, si un escalador desea subir más o menos de la montaña, cuanto tiempo tarda en subir. Debe de resolver el ejercicio. 

def tiempoSubida(distancia, tiempo_base=5, distancia_base=7):
    """
    Calcula el tiempo necesario para subir una montaña proporcionalmente a la distancia.
    :param distancia: Distancia que el escalador desea subir (en metros).
    :param tiempo_base: Tiempo que tarda en subir la distancia base (en horas).
    :param distancia_base: Distancia base que tarda el tiempo_base (en metros).
    :return: Tiempo necesario para subir la distancia deseada (en horas).
    """
    tiempo_total = (distancia * tiempo_base) / distancia_base
    return tiempo_total