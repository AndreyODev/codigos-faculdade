def merge_sort(lista):
    if len(lista) > 1:
        tamanho = len(lista)
        meio = tamanho // 2
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
            
        return merge(esquerda, direita)
    return lista
def merge(esquerda, direita):
    topo_esquerda = 0
    topo_direita = 0
    nova_lista = []
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] < direita[topo_direita]:
            nova_lista.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            nova_lista.append(direita[topo_direita])
            topo_direita += 1
            
    while topo_esquerda < len(esquerda):
        nova_lista.append(esquerda[topo_esquerda])
        topo_esquerda += 1
    while topo_direita < len(direita):
        nova_lista.append(direita[topo_direita])
        topo_direita += 1
        
    return nova_lista        
lista = [2, 1, 7, 2, 6, 4, 1]
resultado = merge_sort(lista)    
print(resultado)