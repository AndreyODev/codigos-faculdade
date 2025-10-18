#8. Contagem de Números Ímpares 
#Escreva um programa que conta e imprime todos os números ímpares entre 1 e 100.
from time import sleep
for c in range(1, 100):
    if c % 2 != 0:
        sleep(1)
        print(c)
    c += 1