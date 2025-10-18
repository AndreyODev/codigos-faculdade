#3. Verificar Par ou Ímpar 
#Peça ao usuário para digitar um número inteiro e informe se o número é par ou ímpar.
N1 = int(input('Digite um número inteiro: '))
if N1 % 2 != 0: 
    print(f'Esse número {N1} é ímpar')
else:
    print(f'Esse número {N1} é par')