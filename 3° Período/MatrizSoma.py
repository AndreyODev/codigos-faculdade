matriz1 = [[1, 2], [3, 7]]
matriz2 =[[1, 2], [3, 7]]

tamanho = 2

def somaMatrizes(m1, m2, tamanho):
    result = []
    for _ in range(tamanho):
        linh = [0] * tamanho
        result.append(linh)
    for i in range(tamanho):
        for j in range(tamanho):
            result [i][j] = m1[i][j] + m2[i][j]
    return result
   
def imprimirMatriz(matriz):
    for linha in matriz:
        print(linha)

resultado = somaMatrizes(matriz1, matriz2, tamanho)
imprimirMatriz(resultado)
