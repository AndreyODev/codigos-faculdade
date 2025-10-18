#3. Crie uma função em Python que leia 80000 números 
#e informe a média dos números. Utilize Funções.
def leia_numero(numeros):
    numeros_lidos = []
    for i in range(numeros):
        numero = i
        numeros_lidos.append(numero)
        return numeros

result = leia_numero(80001)
print(result)

def media(m):
    soma = 0
    for i in range(result):
        soma += i
    return soma/m

r = media(80000)
print(r)