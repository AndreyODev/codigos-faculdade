idade = int(input("Insira sua idade: "))
if idade > 16:
    print("Bem vindo!! Desejo uma excelente experiência!!")
elif idade <= 16:
    responsavel = input("Você está acompanhado por uma pessoa maior de idade? (sim/não)")
    if responsavel == 'sim': 
        print("Bem vindo!! Desejo uma excelente experiência!!")
    else: 
        print ("Infelizmente você não poderá assistir esse filme!!")