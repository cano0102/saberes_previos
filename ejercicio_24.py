# 24) Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y se desea calcular la siguiente información. 

# • Cuanto dinero se ha pagado de intereses en un año. 
# • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año. 
# • Cuanto dinero se ha pagado de intereses en el primer mes. 
# • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses. 

def calcularGastos(monto,plazo=5):
    TASA_FIJA = (monto*5)/100
    interes_trimestral = TASA_FIJA / 4
    interes_tercer_trimestre = interes_trimestral
    interes_mensual = TASA_FIJA / 12
    total = monto + TASA_FIJA * plazo
    return {
        "interes_anual": TASA_FIJA,
        "interes_tercer_trimestre": interes_tercer_trimestre,
        "interes_primer_mes": interes_mensual,
        "total_pagar": total,
    }
