#18. Simulação de Lançamento de Moeda 
#Crie um programa e simule o lançamento de uma moeda (cara ou coroa) e exiba o resultado.
import random
palpite = input('Cara ou Coroa? ').lower()
resultado = random.choice(['cara', 'coroa'])
if palpite == resultado:
    print('Vc acertou, é', resultado)
else:
    print('Vc errou, é', resultado)