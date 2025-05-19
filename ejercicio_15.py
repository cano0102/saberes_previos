# 15. Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por cada cliente: 

# • El monto de la venta, calcule e imprima el IVA.
# • calcule e imprima el total a pagar 
# • lea la cantidad con la que paga el cliente ()solo efectivo, calcule e imprima el cambio. 2


ventas = []

def agregar_venta():
    compra = {}
    
    
    nombre_cliente = str(input("DAME EL NOMBRE DEL CLIENTE: "))
    compra["nombre_cliente"] = nombre_cliente

    numeros_de_productos = int(input("CUANTOS PRODUCTOS VA A COMPRAR: "))
    compra["numeros_de_productos"] = numeros_de_productos

    todos_los_productos = []
    compra["producto"] = todos_los_productos  

    for _ in range(numeros_de_productos):
        producto = {}

        nombre_producto = str(input("DAME EL NOMBRE DEL PRODUCTO: "))
        producto["nombre_producto"] = nombre_producto

        precio_producto = int(input("DAME EL PRECIO DEL PRODUCTO: "))
        producto["precio_producto"] = precio_producto

        todos_los_productos.append(producto)

    
    ventas.append(compra)
    total = sum(prod["precio_producto"] for prod in todos_los_productos)

    IVA = 0.19

    sub_total_iva = total *  IVA
    total += sub_total_iva

    compra["total_compra"] = total


    dinero_entregado_por_el_cliente = float(input("DAME LA CANTIDAD DE DINERO CON EL QUE VAS A PAGAR"))
    compra["dinero_entregado_por_el_cliente"] = dinero_entregado_por_el_cliente

    el_cambio_del_dinero_cliente  =  dinero_entregado_por_el_cliente - total  

    compra["el_cambio_del_dinero_cliente"] = el_cambio_del_dinero_cliente



agregar_venta()