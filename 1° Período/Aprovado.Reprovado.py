p1 = float (input ("Nota da primeira prova: "))
p2 = float (input ("Nota da segunda prova: "))
media = p1 + p2/2
if media >= 7:
    print("Aprovado", media)
else: 
    print("Reprovado", media)
