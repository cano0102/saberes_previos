#4.	Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura si la primera nota tiene un valor del 20%, la segunda del 30% y la última del 50%.
nota1 = float(input("Ingrese la primera nota (20%): "))
nota2 = float(input("Ingrese la segunda nota (30%): "))
nota3 = float(input("Ingrese la tercera nota (50%): "))

definitiva = nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5

print(f"La nota definitiva es: {definitiva:.2f}")