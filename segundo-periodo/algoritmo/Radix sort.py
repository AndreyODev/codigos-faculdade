lista = [123, 142, 807, 263, 123, 41, 90]

maior = max(lista)
p = 1

while maior // p > 0:
    count = [0] * 10
    for e in range(len(lista)):
        menos_signif = (lista[e] // p) % 10
        count[menos_signif] += 1
    for i in range(1, (len(count))):
        count[i] = count[i] + count[i-1]

    lista_ordenada = [0] * len(lista) 
    for i in range(len(lista) -1, -1, -1):
        menos_signif = (lista[i] // p) % 10
        if count[menos_signif] > 0:
            lista_ordenada[count[menos_signif] -1] =  lista[i]
            count[menos_signif] -= 1       

    for i in range(len(lista)):
        lista[i] = lista_ordenada[i]  
    p *= 10

print(lista)








# for e in lista:
#     count[e-menor] += 1

# for i in range(1, (len(count))):
#     count[i] = count[i] + count[i-1]

# lista_ordenada = [0] * len(lista) 
# for i in range(len(lista) -1, -1, -1):
#     e = lista[i] 
#     lista_ordenada[count[e-menor] -1] =  e
#     count[e-menor] -= 1