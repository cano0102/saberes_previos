#2.	Lea dos números y calcule el resultado de su suma, resta, multiplicación y división.
numeros = []
while len(numeros) < 2:
    num = int(input("Ingrese un numero "))
    numeros.append(num)
    
suma = sum(numeros)
print(f"La suma de los numeros {numeros}, es: {suma}")
resta = numeros[0] - numeros[1]
print(f"La resta de los numeros {numeros}, es: {resta}")
multi = numeros[0] * numeros[1]
print(f"La multiplicación de los numeros {numeros}, es: {multi}")
try:
    division = numeros[0] / numeros[1]
except ZeroDivisionError:
    print("No se puede dividir por 0")
else:
    print(f"La division de los numeros {numeros}, es: {division:.2f}")
    