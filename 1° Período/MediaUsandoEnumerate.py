media = 7
alunos = ['Fulano', 'Ciclano', 'Beltrano', 'Gerlano', 'Marlano', 'jesiano']
notas = [0, 2, 10, 9, 8, 5] 
for i, nota in enumerate(notas):
    if nota >= media:
        print(f"{alunos[i]} Aprovado: {nota}")
    else:
        print(f"{alunos[i]} Reprovado: {nota}")