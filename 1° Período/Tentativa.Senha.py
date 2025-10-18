senha_correta = 1234
tentativa = 0
Ltentativa = 3

while tentativa < Ltentativa:
    senha = int(input("Qual a senha? "))
    if senha == senha_correta:
        print("Senha correta")
        break
    else:
        tentativa += 1
        if tentativa < Ltentativa:
            print("Digite novamente")

if tentativa == Ltentativa:
    print("Senha bloqueada")
