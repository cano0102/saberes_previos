#   14. Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de varios artículos (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.



productos_comprados = []
def mostrar_produtos():
    
    print("-----PRODUCTOS A ELEGIR----")
    print("1.BUSO")
    print("2.ZAPATOS")
    print("3.PANTALON")
    print("4.CAMISA")
    print("5.PARA VER EL TOTAL DE LA COMPRA")
    print("6.PARA SALIR")



while True:
    mostrar_produtos()
    
    IVA = 0.19
    opcion = int(input("DAME UN PRODUCTO A COMPRAR: "))
    
    if opcion == 1:

        prod = {}
        prod["nombre"] = "buso"
        prod["precio"] = 150000 
        productos_comprados.append(prod)


        print("COMPRA EXITOSA✅")
    elif opcion == 2:
        prod = {}
        prod["nombre"] = "zapato"
        prod["precio"] = 120000 
        productos_comprados.append(prod)
        print("COMPRA EXITOSA✅")
    
    elif opcion == 3:
        prod = {}
        prod["nombre"] = "pantalon"
        prod["precio"] = 800000 
        productos_comprados.append(prod)

        print("COMPRA EXITOSA✅")

    elif opcion == 4:
        prod = {}
        prod["nombre"] = "camisa"
        prod["precio"] = 60000 
        productos_comprados.append(prod)
        print("COMPRA EXITOSA✅")

    elif opcion == 5:

        suma = sum(suma["precio"] for suma in productos_comprados )

        total_iva = suma * IVA

        total = suma + total_iva


        print("EL TOTAL A PAGAR POR LOS PRODUCTOS ES: " , total)
    
    elif opcion == 6 :
        print("gracias por utilizar este programa , adios")
        break


    else :
        print("opcion invalida")


            

        
        
        mostrar_produtos()