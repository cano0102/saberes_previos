#6.	Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (antes de aplicarle el IVA).
compra = float(input("Ingrese el valor de la compra: "))
descuento = compra * 0.10
valor_con_descuento = compra - descuento
iva = valor_con_descuento * 0.19
total_factura = valor_con_descuento + iva

print(f"Descuento aplicado: {descuento:.2f}")
print(f"Valor con descuento: {valor_con_descuento:.2f}")
print(f"IVA (19%): {iva:.2f}")
print(f"Total a pagar: {total_factura:.2f}")