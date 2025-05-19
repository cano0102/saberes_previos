# 21) Realice un algoritmo que permita realizar el cálculo del siguiente enunciado, se solicita el año de nacimiento del aprendiz, el nombre, la dirección, se requiere conocer la edad de la persona y la información completa ingresada.

from datetime import datetime

def datosUsuario(año,nombre,direccion):
    EDAD = año - datetime.now().year
    print(f"Nombre: {nombre}")
    print(f"Dirección: {direccion}")
    print(f"Año de nacimiento: {año}")
    print(f"Edad: {abs(EDAD)} años")

datosUsuario(2006,"Brandon","CRA 42N")
