import string
import random
senha = []
num = string.digits
numeros = int(input('é quantos numeros ? =>'))
for digito in range (numeros):
    aleatorio = random.choice(num)
    senha += aleatorio
senha_aleatoria = random.shuffle(senha)
print(''.join(senha))
    