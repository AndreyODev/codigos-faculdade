import string
import random
senha = []
num = string.digits
letra = string.ascii_lowercase
letra_m = string.ascii_uppercase
carc = string.punctuation
letras = int(input('Quantas  letras você quer na sua senha =>'))
caracteres = int(input('Quantos caractesres você vai querer na sua senha =>'))
numeros = int(input('é quantos numeros ? =>'))
for digito in range (numeros):
    aleatorio1 = random.choice(num)
    senha += aleatorio1
for digito in range (letras):
    aleatorio2 = random.choice(letra)
    senha += aleatorio2

for digito in range (caracteres):
    aleatorio4 = random.choice(carc)
    senha += aleatorio4
    
aleatorio_senha = random.shuffle(senha)

print(''.join(senha))
