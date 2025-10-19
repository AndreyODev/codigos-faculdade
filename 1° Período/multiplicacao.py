

i = 0
while True:
     qtd_numero = int(input('Digite a quantidade de numero desejada: '))
     if qtd_numero >=100: 
        i = i + 1
        total = qtd_numero * i 
        print(f'{qtd_numero} x {i} = {total }')
