#9. Verificar Número Primo 
#Peça ao usuário para digitar um número e verifique se ele é primo.

n = int(input('Digite um número: '))
primos = []
for c in range(1, n +1):
    if n % c == 0:
        primos.append(c)
    else:
        pass
        
if len(primos) == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')