# 1.	Lea tres números y calcule el resultado de su suma.
numeros = []
while len(numeros) < 3:
    num = int(input("Ingrese un numero "))
    numeros.append(num)
    
suma = sum(numeros)
print(f"La suma de los numeros {numeros}, es: {suma}")