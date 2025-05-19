#Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.

horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

segundos_totales = (horas * 3600) + (minutos * 60) + segundos
print("La cantidad total de segundos es:", segundos_totales)
