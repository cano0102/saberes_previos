#Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 2% mensual.

capital_inicial = float(input("Ingrese el capital inicial: "))
interes = 0.02
capital_final = capital_inicial + (capital_inicial * interes)
print("El capital final después de un mes es:", round(capital_final, 2))
