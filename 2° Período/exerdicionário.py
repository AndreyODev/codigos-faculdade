clientes = {"nome": [], "email": [], "telefone": [], "endereco": []}

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = {"nome": nome, "email": email, "telefone": telefone, "endereco": endereco}
    clientes["nome"].append(cliente["nome"])
    clientes["email"].append(cliente["email"])
    clientes["telefone"].append(cliente["telefone"])
    clientes["endereco"].append(cliente["endereco"])
    print(f"O cliente {nome} foi adicionado com sucesso")
def exibir_clientes():
    print(clientes)
def buscar_cliente(email):
    for i, cliente in enumerate(clientes["email"]):
        if cliente == email:
            print(f"Cliente encontrado -- nome: {clientes['nome'][i]}, email: {clientes['email'][i]}, telefone: {clientes['telefone'][i]}, endereço: {clientes['endereco'][i]}")
            return
    print("Cliente não encontrado")
def remover_cliente(email):
    for i, cliente in enumerate(clientes["email"]):
        if cliente == email:
            print(f"O cliente {clientes['email'][i]} foi removido")
def teste():
    adicionar_cliente("Andrey", "andrey@gm", "2222", "rua 5")
    exibir_clientes()
    buscar_cliente("andrey@gm")
    remover_cliente("andrey@gm")


def menu():
    while True:
        print("------------------------")
        print("Digite 1 para add")
        print("Digite 2 para exib")
        print("Digite 3 para busc")
        print("Digite 4 para remove")
        print("Digite 5 para teste")
        print("Digite 6 para sair")
        print("------------------------")
        opc = input("Informe um número: ")
        if opc == "1":
            nome = input("Informe um nome: ")
            email = input("Informe um email: ") 
            telefone = input("Informe um telefone: ") 
            endereco = input("Informe um endereço: ") 
            adicionar_cliente(nome, email, telefone, endereco)
        elif opc == "2":
            exibir_clientes()
        elif opc == "3":
            email = input("Informe um email: ")
            buscar_cliente(email)
        elif opc == "4":
            email = input("Informe um email: ")
            remover_cliente(email)
        elif opc == "5":
            teste()
        elif opc == "6":
            print("Saindo......")
            break

menu()