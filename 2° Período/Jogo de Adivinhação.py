#20. Jogo de Adivinhação 
#Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 
#e o usuário deve tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor que a tentativa do usuário.
import random
for i in range(100):
    n = random.randint(1, 100)
    print("Tente adivinhar o número que estou pensando, entre 1 e 100.")
    palpite = int(input("Digite o seu palpite: "))
    if palpite > n:
        print(f"O numero escolhido é {n}, e é menor do que o que vc escolheu")
    elif palpite == n:
         print("Acertou")
    else:
        print(f"O numero escolhido é {n}, e é maior do que o que vc escolheu")