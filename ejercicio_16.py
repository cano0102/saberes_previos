# 16. Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le corresponde en un día trabajado, teniendo en cuenta que tiene derecho a el 19% del total recaudado.



def calcular_cuanto_le_corresponde_por_lo_recaudado():
    

    total_recaudado = float(input("DAME EL TOTAL RECAUDADO DEL DIA"))

    lo_que_le_corresponde = (total_recaudado*19) / 100

    print("LO QUE TE CORRESPONDE ES :",lo_que_le_corresponde)
    

calcular_cuanto_le_corresponde_por_lo_recaudado()