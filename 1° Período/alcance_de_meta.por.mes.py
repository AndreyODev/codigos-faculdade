alcance_de_meta = []
meta = 50
semestre_1 = [20, 50, 100, 300, 2, 1]
semestre_2 = [12, 100, 3, 40, 49, 70]
semestre_1.extend(semestre_2)
ano = semestre_1
meses = ["jan", "fev", "mar", "abr", "maio", "jun", "jul", "agos", "setem", "out", "nov", "dezem"]

print("Meses que atingiram a meta:")
for x, ano in enumerate(ano):
    if ano >= meta:
        print(f"{meses[x]}: {ano}") 