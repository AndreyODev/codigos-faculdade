#15. Números Pares em uma Lista 
#Dada uma lista de números, crie um programa que exiba apenas os números pares
listaN = [9, 7, 8, 5, 4, 6]
pares = []
for n in listaN:
    if n % 2 == 0:
        pares.append(n)
print(pares)
