alcance_de_meta = []
meta = 50
semestre_1 = [20, 50, 100, 300, 2, 1]
semestre_2 = [12, 100, 3, 40, 49, 70]
semestre_1.extend(semestre_2)
ano = semestre_1

for mes in ano:
    if mes >= meta: 
        alcance_de_meta.append(mes)
print(alcance_de_meta)
