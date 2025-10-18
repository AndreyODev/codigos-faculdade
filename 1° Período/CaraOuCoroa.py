import random
palpite = input('Cara ou Coroa? ').lower()
resultado = random.choice(['cara', 'coroa'])
if palpite == resultado:
    print('Vc acertou, é', resultado)
else:
    print('Vc errou, é', resultado)
    

