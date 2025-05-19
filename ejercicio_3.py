#3.	Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura. > <
notas = []
while len(notas) < 3:
    nota = float(input("Ingrese sus notas "))
    if 1.0 <= nota <= 5.0:
        notas.append(nota)
    else:
        print("La nota debe estar entre 0 y 5. Intente de nuevo.")
    
definitiva = sum(notas) / len(notas)
print(f"La nota definitiva de la asignatura es: {definitiva:.2f}")
