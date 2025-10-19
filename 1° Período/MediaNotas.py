mediaA = 7
notas = [0, 10, 10, 10, 9, 8, 5, 4, 2, 6, 6, 5, 4]
soma_notas = sum(notas)
numeros_alunos = len(notas)
mediaT = soma_notas/numeros_alunos
contador = 0
for nota in notas:
    if nota <= mediaA:
        contador += 1
print(f"A media da turma é {mediaT}", f"e o numero de notas menores ou igual a 7 é {contador}")