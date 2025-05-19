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