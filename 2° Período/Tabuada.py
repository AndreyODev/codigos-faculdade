#11. Tabuada 
#Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.
from time import sleep
N = int(input('Digite um número: '))
c = N
for T in range(1, 11):
    multiplicacao = N * T
    sleep(1)
    print(f'{c} x {T} = {multiplicacao}')