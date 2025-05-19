# 13. Dada las horas trabajadas de una persona y el valor por hora. Calcular su salario e imprimirlo. 

def salario():
    
    VALOR_DE_HORAS = 10000
    horas_trabajadas = int(input("DAME LAS HORAS TRABAJADAS "))
    total_de_salario = VALOR_DE_HORAS * horas_trabajadas

    print("EL SALARIO TUYO ES DE " , total_de_salario )

salario()