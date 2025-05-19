#   12. Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.


def  porcentajes():

    total_estudiantes = int(input("DAME EL NUMERO TOTAL DE ESTUDIANTES: "))
    
    hombres = int(input("DAME EL NUMERO DE ESTUDIANTES DE HOMBRE"))

    mujeres = total_estudiantes - hombres



    porcentaje_uno= (total_estudiantes/hombres) * 100
    porcentaje_dos = (total_estudiantes/mujeres) * 100

    print("EL PORCENTAJES DE HOMBRES ES:", porcentaje_uno , "EL PORCENTAJE DE MUJERES ES:",porcentaje_dos)

porcentajes()
