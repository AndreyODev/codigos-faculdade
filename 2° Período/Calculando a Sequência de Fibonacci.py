#17. Calculando a Sequência de Fibonacci 
#Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.
anterior = 0
proximo = 1
atual = 1
for i in range(10):
    print(proximo, end=" ")
    proximo = atual + anterior
    anterior = atual
    atual = proximo