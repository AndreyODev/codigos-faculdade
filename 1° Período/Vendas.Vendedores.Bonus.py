vendedor_1 = 700
vendedor_2 = 1200
vendedor_3 = 2000
meta = 100
N_de_Vendav1 = float (input("Digite o número de vendas do vendedor 1? "))
if N_de_Vendav1 < meta:
    print ("O sálario do vendedor 1 vai ser o mesmo")
elif N_de_Vendav1 >= meta and N_de_Vendav1 < 201:
    bonus = (float (vendedor_1)) * 10/100
    salario = vendedor_1 + bonus 
    print ("O vendedor 1 receberá 10% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario)
elif N_de_Vendav1 > 200:
    bonus2 = (float (vendedor_1)) * 40/100
    salario2 = vendedor_1 + bonus2
    print ("o fvendedor 1 receberá 40% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario2)

N_de_Vendav2 = float (input("Digite o número de vendas do vendedor 2? "))
if N_de_Vendav2 < meta:
    print ("O sálario do vendedor 2 vai ser o mesmo")
elif N_de_Vendav2 >= meta and N_de_Vendav2 < 201:
    bonus = (float (vendedor_2)) * 10/100
    salario = vendedor_2 + bonus 
    print ("o vendedor 2 receberá 10% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario)
elif N_de_Vendav2 > 200:
    bonus2 = (float (vendedor_2)) * 40/100
    salario2 = vendedor_2 + bonus2
    print ("O vendedor 2 receberá 40% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario2)

N_de_Vendav3 = float (input("Digite o número de vendas do vendedor 3? "))
if N_de_Vendav3 < meta:
    print ("O sálario do vendedor 3 vai ser o mesmo")
elif N_de_Vendav3 >= meta and N_de_Vendav3 < 201:
    bonus = (float (vendedor_3)) * 10/100
    salario = vendedor_3 + bonus 
    print ("O vendedor 3 receberá 10% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario)
elif N_de_Vendav3 > 200:
    bonus2 = (float (vendedor_3)) * 40/100
    salario2 = vendedor_3 + bonus2
    print ("O vendedor 3 receberá 40% em cima do seu salário de bonus.Sendo assim seu sálario será R$ ",salario2)
     

