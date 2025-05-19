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