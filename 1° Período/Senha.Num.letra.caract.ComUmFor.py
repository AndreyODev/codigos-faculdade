import random
import string
senha = []
carac = string.printable
qnt = int(input('Quantos dígitos deve conter a sua senha? '))
for digito in range(qnt):
    aleatorio = random.choice(carac)
    senha += aleatorio
    aleatorio_senha = random.shuffle(senha)
print('Sua senha é', ''.join(senha))
