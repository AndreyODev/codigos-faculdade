def busca(lista, chave):
    i = 0
    for n in lista:
        if n == chave:
            return i
        i += 1 
    return -1

result = busca([1, 2, 3, 4, 5, 6], 5)
print(result)