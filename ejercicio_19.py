# 19) Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.  Hacer un algoritmo que:
# Muestre el nombre
# Muestre el programa de formación

#
# Se debe calcular y mostrar su promedio final.





escuela = []

def registros_de_estudiantes():
    estudiantes= {}
    nombre = str(input("EL NOMBRE DEL ESTUDIANTE: "))
    estudiantes["nombre_estudiante"] = nombre
    edad = int(input("EDAD DEL ESTUDIANTE"))
    estudiantes["edad"] = edad

    todas_las_notas = []

    while True:
        notas = float(input("DAME UNA NOTA (-1 para salir)"))

        if notas == -1:
            print("saliendo...")
            break
        else:
            todas_las_notas.append(notas)
            estudiantes["nota"] = todas_las_notas
            continue
    materias =  ["matematicas","ingles","español"]
    estudiantes["materias "] = materias
    escuela.append(estudiantes)
    print(escuela)

def consultar_un_estudiantes():
    nombre_a_consultar = str(input("dame el nombre del estudiante"))
    for estudiante in escuela:
        if estudiante["nombre_estudiante"] == nombre_a_consultar:
            print("si esta ",nombre_a_consultar)
        else:
            print("no esta ")

def reporte():
    total_estudiantes = len(escuela)
    print("estos son todos los estudiantes " , total_estudiantes)

    suma_de_notas = sum(notas for estudiante in escuela for notas in estudiante["nota"])
    print("la suma de todas las notas es ",suma_de_notas)

    numero_de_notas = sum(len(estudiante["nota"]) for estudiante in escuela )
    print("el numero de notas es " , numero_de_notas)

    

    promedio = suma_de_notas / numero_de_notas
    print("el promedio es" ,  promedio)
    
    
    
    
    






def mostrar_estudiantes():
    for estudiantes in escuela:
        print(estudiantes)

def eliminar():
    nombre_a_eliminar = str(input("dame el nombre del estudiante"))
    for estudiante in escuela:
        if  estudiante["nombre_estudiante"]== nombre_a_eliminar:
            escuela.remove(estudiante)
            
        else:
            print("no esta ")



def menu():
    print("---ELIGE UNA OPCION---")
    print("1.Para agregar estudiantes")
    print("2.Para mostrar todos los estudiantes")
    print("3.Para eliminar un estudiante")
    print("4.Para consultar estudiantes")
    print("5.Para el reporte")
    print("6.Para salir")



while True:
    menu()
    opcion = int(input("DAME UN OPCION: "))

    if opcion == 1:
        registros_de_estudiantes()
    elif opcion == 2:
        mostrar_estudiantes()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        consultar_un_estudiantes()
    elif opcion == 5:
        reporte()
        
    elif opcion == 6:
        print("gracias")
        break
    else:

        print("opcion no validad")