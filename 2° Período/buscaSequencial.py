def buscaSequencial(lista, chave):
    i = 0
    for n in lista:
        if n == chave:
            return i
        i += 1
    return -1  

chave = 45
lista = [20, 5, 24, 67, 45, 1, 76, 21, 11]
pos = buscaSequencial(lista, chave)  
if pos != -1:
    print("Posição da chave", chave, "na lista:", pos)
else:
    print("A chave", chave, "não se encontra na lista")