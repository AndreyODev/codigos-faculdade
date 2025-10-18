#4. Calculadora Simples 
#Crie um programa que peça dois números e a operação desejada (+, -, *, /) e exiba o resultado.
N1 = float(input('Informe um número: '))
N2 = float(input('Informe outro número: '))
O = input('Gostaria de usar qual operação [+, -, *, /]? ')
if O == '+':
    soma = N1 + N2
    print(f'{soma:.1f}')
elif O == '-':
    subtracao = N1 - N2
    print(f'{subtracao:.1f}')
elif O == '*':
    multiplicacao = N1 * N2
    print(f'{multiplicacao:.1f}')
elif O == '/':
    divisao = N1 / N2
    print(f'{divisao:.1f}')