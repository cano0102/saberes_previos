# 10. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.


def  total_cuenta():

    cuenta = float(input("DAME EL EL VALOR DE TU COMPRA: "))

    descuento = cuenta*15/100

    total = cuenta - descuento 
    print("El MONTO A PAGAR ES ",total)


total_cuenta()