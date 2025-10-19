nome = ""
while True:
    nome = input("Digite um nome com mais de 2 letras: ")
    if nome.isalpha() and len(nome) > 2:
        print('Nome válido')
        break
    else:
        print("O nome deve ter mais de 2 letras. Tente novamente.")

idade = int(input("Quantos anos vc tem? "))
print(f"Eu tenho {idade} anos")

while True:
    salario = float(input("Informe seu salario: "))
    if salario >= 0:
        print("Ok")  
        break
    else:
        print("informe de novo por favor")

while True:
    sexo_biologico = input("Informe seu sexo biologico(F: Femino ou M: Masculino): ")
    if sexo_biologico == "f" or sexo_biologico == "F" or sexo_biologico == "M" or sexo_biologico == "m":
        print("Show")
        break
    else:
        print("Informe novamente seu sexo biologico")


