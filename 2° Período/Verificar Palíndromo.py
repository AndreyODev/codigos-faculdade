#19. Verificar Palíndromo 
#Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente).
palavra = str(input('Digite um palavra: ')).upper()
inverso = ''
for letra in range(len(palavra) -1, -1, -1):
    inverso += palavra[letra] 
    print(f'{palavra[letra]}', end='')
if inverso == palavra:
    print(' é um palíndromo!')
else:
    print(' nao é um palíndromo!')