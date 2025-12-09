def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista) -1
    while inicio <= fim:
        meio = (inicio+fim) //2
        if lista[meio] == chave:
            return meio
        if lista[meio] > chave:
            fim = meio -1
        else:
            inicio = meio +1
    return -1
chave = 15
lista = [3, 4, 9, 23, 45, 67, 89]
pos = buscaBinaria(lista, chave)
if pos != -1:
    print("Posição da chave", chave, "na lista:", pos)
else:
    print("A chave", chave, "não se encontra na lista")