# 10. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.


def  total_cuenta():

    cuenta = float(input("DAME EL EL VALOR DE TU COMPRA: "))

    descuento = cuenta*15/100

    total = cuenta - descuento 
    print("El MONTO A PAGAR ES ",total)


total_cuenta()


#    11. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.  Dicha calificación se compone de los siguientes porcentajes:
# 	55% del promedio de sus tres calificaciones parciales.
#  	30% de la calificación del examen final. 
# 	15% de la calificación de un trabajo final



def calificacion_final():
    
    parcial_uno = float(input("DAME LA NOTA DEL PARCIAL 1: "))
    parcial_dos = float(input("DAME LA NOTA DEL PARCIAL 2: "))
    parcial_tres = float(input("DAME LA NOTA DEL PARCIAL 3: "))

    promedio_de_parciales = (parcial_uno+parcial_dos+parcial_tres) / 3 

    calificacion_del_examen_final = float(input("DAME LA CALIFICACION DE EXAMEN FINAL: "))
    calificacion_de_trabajo_final  = float(input("DAME LA CALIFICACION DEl TRABAJO FINAL: "))

    calificacion_finall = (promedio_de_parciales * 0.55) + (calificacion_del_examen_final * 0.30) + (calificacion_de_trabajo_final * 0.15)

    print("LA CALIFICACION FINAL ES: ",calificacion_finall)

calificacion_final()


#   12. Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.


def  porcentajes():

    total_estudiantes = int(input("DAME EL NUMERO TOTAL DE ESTUDIANTES: "))
    
    hombres = int(input("DAME EL NUMERO DE ESTUDIANTES DE HOMBRE"))

    mujeres = total_estudiantes - hombres



    porcentaje_uno= (total_estudiantes/hombres) * 100
    porcentaje_dos = (total_estudiantes/mujeres) * 100

    print("EL PORCENTAJES DE HOMBRES ES:", porcentaje_uno , "EL PORCENTAJE DE MUJERES ES:",porcentaje_dos)







