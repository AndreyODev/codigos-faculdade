clientes = []
reservas = []
quartos = {"01": "Disponível", "02": "Disponível", "03": "Disponível", "04": "Disponível"}

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")

    cliente = {"nome": nome, "email": email, "telefone": telefone, "senha": senha}
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def login():
    email = input("Digite seu E-mail: ")
    senha = input("Digite sua Senha: ")

    for cliente in clientes:
        if cliente["email"] == email and cliente["senha"] == senha:
            print(f"Login bem-sucedido! Bem-vindo(a), {cliente['nome']}!")
            return cliente  
    print("E-mail ou senha incorretos!")

def reservar_quarto(cliente):
    if cliente is None:
        print("Você precisa fazer login para reservar um quarto.")
        return

    print("Quartos disponíveis: ")
    for numero, status in quartos.items():
        if status == "Disponível":
            print(f"{numero}: {status}")

    quarto = input("Digite o número do quarto que deseja reservar: ")
    if quarto in quartos and quartos[quarto] == "Disponível":
        check_in = input("Data de Check-in (DD/MM/AAAA): ")
        check_out = input("Data de Check-out (DD/MM/AAAA): ")
        reserva = {"cliente": cliente["nome"], "quarto": quarto, "check_in": check_in, "check_out": check_out}
        reservas.append(reserva)
        quartos[quarto] = "Ocupado"
        print(f"Reserva realizada com sucesso para o quarto {quarto}.")
    else:
        print("Quarto não disponível.")

def gerenciar_reservas():
    print("Reservas:")
    for reserva in reservas:
        print(f"Cliente: {reserva['cliente']}, Quarto: {reserva['quarto']}, Check-in: {reserva['check_in']}, Check-out: {reserva['check_out']}")

    acao = input("Deseja cancelar alguma reserva? (sim/não): ")
    if acao.lower() == "sim":
        quarto = input("Digite o número do quarto: ")
        for reserva in reservas:
            if reserva["quarto"] == quarto:
                print(f"Reserva encontrada: {reserva}")
                cancelamento = input("Confirmar cancelamento? (sim/não): ")
                if cancelamento.lower() == "sim":
                    reservas.remove(reserva)
                    quartos[reserva["quarto"]] = "Disponível"
                    print(f"Reserva do quarto {quarto} cancelada com sucesso!")
                break
        else:
            print("Reserva não encontrada.")

def pagamento(cliente):
    if cliente is None:
        print("Você precisa fazer login para realizar o pagamento.")
        return

    print(f"Realizando pagamento para o cliente {cliente['nome']}.")
    metodo_pagamento = input("Escolha o método de pagamento (1 para Cartão de Crédito, 2 para Cartão de Débito): ")

    if metodo_pagamento == "1" or metodo_pagamento == "2":
        print("Pagamento realizado com sucesso!")
    else:
        print("Método de pagamento inválido!")

def menu():
    cliente_logado = None
    while True:
        print("\nMenu de opções:")
        print("1. Cadastro de Cliente")
        print("2. Login")
        print("3. Reservar Quarto")
        print("4. Gerenciar Reservas")
        print("5. Pagamento")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cliente_logado = login()
        elif opcao == "3":
            reservar_quarto(cliente_logado)
        elif opcao == "4":
            gerenciar_reservas()
        elif opcao == "5":
            pagamento(cliente_logado)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

menu()