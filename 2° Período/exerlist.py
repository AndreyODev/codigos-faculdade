clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"O cliente {nome} foi adicionado com sucesso")
def exibir_clientes():
    print(clientes)
def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado -- nome: {cliente[0]}, email: {cliente[1]}, telefone: {cliente[2]}, endereço: {cliente[3]}")
        else:
            print("Cliente não encontrado")
def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"O cliente {email} foi removido")
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