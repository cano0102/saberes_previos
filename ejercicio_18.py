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