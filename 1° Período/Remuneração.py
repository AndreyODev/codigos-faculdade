vendas = float (input("Número de vendas: ")) 
remuneração = 1000
adicional = remuneração * 25/100
adicional1 = remuneração + adicional 
desconto = remuneração * 30/100
desconto1 = remuneração - desconto 
if vendas >= 50:
    print (f"Terá um adicional de 25% em cima da sua remuneração, sendo assim receberá {adicional1}")
elif vendas < 5: 
    print (f"Terá um desconto de 30% em cima da sua remuneração, sendo assim receberá {desconto1}")
elif vendas >= 5 and vendas <= 49:
    print ((f"A remuneração será normal, sendo assim receberá {remuneração}"))

