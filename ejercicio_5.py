5#.	Lea la distancia (en kilómetros) recorrida por un auto, el tiempo (en horas) en que la recorrió y calcule la velocidad a la cual se desplazaba el auto (V=D/T).
distancia = float(input("Ingrese la distancia recorrida (en kilómetros): "))
tiempo = float(input("Ingrese el tiempo empleado (en horas): "))

if tiempo != 0:
    velocidad = distancia / tiempo
    print(f"La velocidad del auto es {velocidad:.2f} km/h")
else:
    print("El tiempo no puede ser cero.")