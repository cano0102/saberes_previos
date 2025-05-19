


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

porcentajes()


# 13. Dada las horas trabajadas de una persona y el valor por hora. Calcular su salario e imprimirlo. 

def salario():
    
    VALOR_DE_HORAS = 10000
    horas_trabajadas = int(input("DAME LAS HORAS TRABAJADAS "))
    total_de_salario = VALOR_DE_HORAS * horas_trabajadas

    print("EL SALARIO TUYO ES DE " , total_de_salario )

salario()



#   14. Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de varios artículos (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.



productos_comprados = []
def mostrar_produtos():
    
    print("-----PRODUCTOS A ELEGIR----")
    print("1.BUSO")
    print("2.ZAPATOS")
    print("3.PANTALON")
    print("4.CAMISA")
    print("5.PARA VER EL TOTAL DE LA COMPRA")
    print("6.PARA SALIR")



while True:
    mostrar_produtos()
    
    IVA = 0.19
    opcion = int(input("DAME UN PRODUCTO A COMPRAR: "))
    
    if opcion == 1:

        prod = {}
        prod["nombre"] = "buso"
        prod["precio"] = 150000 
        productos_comprados.append(prod)


        print("COMPRA EXITOSA✅")
    elif opcion == 2:
        prod = {}
        prod["nombre"] = "zapato"
        prod["precio"] = 120000 
        productos_comprados.append(prod)
        print("COMPRA EXITOSA✅")
    
    elif opcion == 3:
        prod = {}
        prod["nombre"] = "pantalon"
        prod["precio"] = 800000 
        productos_comprados.append(prod)

        print("COMPRA EXITOSA✅")

    elif opcion == 4:
        prod = {}
        prod["nombre"] = "camisa"
        prod["precio"] = 60000 
        productos_comprados.append(prod)
        print("COMPRA EXITOSA✅")

    elif opcion == 5:

        suma = sum(suma["precio"] for suma in productos_comprados )

        total_iva = suma * IVA

        total = suma + total_iva


        print("EL TOTAL A PAGAR POR LOS PRODUCTOS ES: " , total)
    
    elif opcion == 6 :
        print("gracias por utilizar este programa , adios")
        break


    else :
        print("opcion invalida")


            

        
        
        mostrar_produtos()


# 15. Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por cada cliente: 

# • El monto de la venta, calcule e imprima el IVA.
# • calcule e imprima el total a pagar 
# • lea la cantidad con la que paga el cliente ()solo efectivo, calcule e imprima el cambio. 2


ventas = []

def agregar_venta():
    compra = {}
    
    
    nombre_cliente = str(input("DAME EL NOMBRE DEL CLIENTE: "))
    compra["nombre_cliente"] = nombre_cliente

    numeros_de_productos = int(input("CUANTOS PRODUCTOS VA A COMPRAR: "))
    compra["numeros_de_productos"] = numeros_de_productos

    todos_los_productos = []
    compra["producto"] = todos_los_productos  

    for _ in range(numeros_de_productos):
        producto = {}

        nombre_producto = str(input("DAME EL NOMBRE DEL PRODUCTO: "))
        producto["nombre_producto"] = nombre_producto

        precio_producto = int(input("DAME EL PRECIO DEL PRODUCTO: "))
        producto["precio_producto"] = precio_producto

        todos_los_productos.append(producto)

    
    ventas.append(compra)
    total = sum(prod["precio_producto"] for prod in todos_los_productos)

    IVA = 0.19

    sub_total_iva = total *  IVA
    total += sub_total_iva

    compra["total_compra"] = total


    dinero_entregado_por_el_cliente = float(input("DAME LA CANTIDAD DE DINERO CON EL QUE VAS A PAGAR"))
    compra["dinero_entregado_por_el_cliente"] = dinero_entregado_por_el_cliente

    el_cambio_del_dinero_cliente  =  dinero_entregado_por_el_cliente - total  

    compra["el_cambio_del_dinero_cliente"] = el_cambio_del_dinero_cliente



agregar_venta()


# 16. Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le corresponde en un día trabajado, teniendo en cuenta que tiene derecho a el 19% del total recaudado.



def calcular_cuanto_le_corresponde_por_lo_recaudado():
    

    total_recaudado = float(input("DAME EL TOTAL RECAUDADO DEL DIA"))

    lo_que_le_corresponde = (total_recaudado*19) / 100

    print("LO QUE TE CORRESPONDE ES :",lo_que_le_corresponde)




#   17. Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una   empresa. La colilla debe mostrar:
#     • El Salario del Empleado 
#     • El Valor de Ahorro mensual programado.
#     • La suma a deducir por aporte a la Salud (EPS) 12,5 %
#     • La suma a deducir por aporte al Fondo de Pensiones  16%
#     • Total a Recibir 
#     • Toda la información que debe proveer el usuario del programa es el  Salario del Empleado y el Valor de Ahorro mensual programado. El programa debe calcular y devolver el resto de los datos.4


def pago_de_los_empledos():
    
    empleado = {}
    salario_empleado = float(input("DAME EL SALARIO MENSUAL: "))
    empleado["salario_sin_descuentos"] = salario_empleado

    ahorro_mesual_programado = float(input("DAME EL AHORRO MENSUAL PROGRAMADO: "))
    empleado["descuento_de_el ahorro"] = ahorro_mesual_programado


    DESCUENTO_EPS = 12.5
    empleado["descuento_EPS"] = DESCUENTO_EPS 

    PENSION = 16
    empleado["descuento_pension"] = PENSION
   

    total_ahorro = salario_empleado - ahorro_mesual_programado 

    total_eps = (salario_empleado * DESCUENTO_EPS) / 100
    total_pension = (salario_empleado * PENSION) / 100


    sueldo_final = salario_empleado - total_eps - total_pension - ahorro_mesual_programado


    empleado["sueldo_final"] = sueldo_final


pago_de_los_empledos()








# 18. En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de la siguiente forma 

# • Primera cuota: 40% 
# • Segunda cuota: 25%
# •  Tercera cuota: 20% 
# • Cuarta cuota: 15% 


# Diga cuanto es el valor que tiene que pagar por cuota un estudiante.


def valor_matricula():
    
    valor_de_matricula = float(input("DAME EL VALOR DE TU MATRUCULA: "))

    valor_matricula_40 = (valor_de_matricula * 40) / 100

    print("EL VALOR DE LA PRIMERA PATER ES:", valor_matricula_40)

    valor_matricula_25 = (valor_de_matricula * 25) / 100

    print("EL VALOR DE LA PRIMERA PATER ES:", valor_matricula_25)

    valor_matricula_20= (valor_de_matricula * 20) / 100

    print("EL VALOR DE LA PRIMERA PATER ES:", valor_matricula_20)

    valor_matricula_15 = (valor_de_matricula * 15) / 100

    print("EL VALOR DE LA PRIMERA PATER ES:", valor_matricula_15)


valor_matricula()


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







