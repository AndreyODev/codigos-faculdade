salario = 2700
bonus = salario *10/100
novosalario = salario + bonus

bonus2 = salario *30/100
novosalario2 = salario + bonus2

vendasvendedor = float (input("Qual foi o número de vendas? "))
if vendasvendedor > 100 and vendasvendedor < 300:
    print (f"O vendedor irá recebe 10% em cima do seu sálario, sendo assim seu sálario será R$ {novosalario}")
if vendasvendedor > 300:
    print (f"O vendedor irá recebe 15% em cima do seu sálario, sendo assim seu sálario será R$ {novosalario2}")
else: 
    print ("O sálario permanecera o mesmo")