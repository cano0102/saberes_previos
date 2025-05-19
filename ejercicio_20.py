# Ingresar el precio de compra unitario de un producto y la cantidad de compra de dicho producto y un descuento. 
# Calcular y mostrar el subtotal, el monto del IVA que es el 19% del subtotal, y el precio neto (precio parcial con el Monto del IVA).

def calcularTotal(precio, descuento, cantidad):
    IVA = 0.19
    subtotal = precio * cantidad
    monto_iva = subtotal * IVA 
    total = subtotal + monto_iva - descuento 
    return f"Subtotal: {subtotal:.2f}, Monto IVA: {monto_iva:.2f}, Total a pagar: {total:.2f}"

