lista = [2, 4, 1, 3, 2, 4, 5]

menor = min(lista)
maior = max(lista)
t = maior - menor + 1

count = [0] *  t

for e in lista:
    count[e-menor] += 1

for i in range(1, (len(count))):
    count[i] = count[i] + count[i-1]

lista_ordenada = [0] * len(lista) 
for i in range(len(lista) -1, -1, -1):
    e = lista[i] 
    lista_ordenada[count[e-menor] -1] =  e
    count[e-menor] -= 1

print(lista_ordenada)

