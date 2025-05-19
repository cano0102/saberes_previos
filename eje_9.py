#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

comision = 0.10
comision_venta1 = venta1 * comision
comision_venta2 = venta2 * comision
comision_venta3 = venta3 * comision

total_comisiones = comision_venta1 + comision_venta2 + comision_venta3
sueldo_total = sueldo_base + total_comisiones

print("El total de comisiones es:", round(total_comisiones, 2))
print("El sueldo total del vendedor es:", round(sueldo_total, 2))
