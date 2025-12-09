def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]
    
    left = []
    right = []
    for e in lista[:-1]:
        if pivo >= e:
            left.append(e)
        else: 
            right.append(e)

    return quick_sort(left) + [pivo] + quick_sort(right)
lista = [3, 6, 8, 10, 1, 2, 1]
result = quick_sort(lista)
print(result)  

















#     for i in lista: 
#         pivo = lista[-1]
#         esquerda = 0
#         direita = lista[0] 
#         if pivo >= i:
#             esquerda = i+1
#         else: 
#             direita = i-1
#         direita, esquerda = esquerda, direita
#     return esquerda, direita
# result = quickSort(lista)
# print(result)