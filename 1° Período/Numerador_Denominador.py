numerador = 0
denominador = 0
n = int(input("Quantas notas? "))
for x in range(n):
    nota = float(input(f"Nota {x+1}: "))
    peso = int(input(f"Peso da nota {x+1}: "))
    numerador += nota * peso
    denominador += peso

mediap = numerador / denominador
print(f"A média ponderada é {mediap}")