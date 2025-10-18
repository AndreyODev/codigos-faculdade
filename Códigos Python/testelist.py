list = []
def adicionar_cliente(nome, email, telefone, endereco):
    lista = [nome, email, telefone, endereco]
    list.append(lista)
    print("Cliente adicionado com sucesso")
def exibir_clientes():
    print(list)
def buscar_cliente(email):
    for cliente in list:
        if cliente[1] == email:
            print(f"Cliente encontrado -- nome: {cliente[0]}, email: {cliente[1]}, telefone: {cliente[2]}, endereço: {cliente[3]}")
def remover_cliente(email):
    for cliente in list:
        if cliente[1] == email:
            list.remove(cliente)
            print("Email removido")
def menu():
    while True:
        print("------------------------")
        print("Digite 1 para add")
        print("Digite 2 para exibir")
        print("Digite 3 para buscar")
        print("Digite 4 para remove")
        print("Digite 5 para sair")
        print("------------------------")
        opc = input("Informe um número: ")
        if opc == "1":
            nome = input("Informe seu nome: ")
            email = input("Informe seu email: ")
            telefone = input("Informe seu telefone: ")
            endereco = input("Informe seu endereco: ")    
            adicionar_cliente(nome, email, telefone, endereco)
        elif opc == "2":
            exibir_clientes()
        elif opc == "3":
            email = input("Informe o email que deseja buscar: ")
            buscar_cliente(email)
        elif opc == "4":
            email = input("Informe o email que deseja remove: ")
            remover_cliente(email)
        elif opc == "5":
            print("Saindo.......")
menu()
