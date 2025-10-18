produto = input ("Qual o nome do produto: ")
preco = float (input("Qual o preço do produto: "))
aumento = preco * 40/100
aumento2 = preco + aumento 
print (f"O {produto} vai custar " f"{aumento2} reais com 40% de aumento")