lista = []

def cadastrar_entrega(codigo, fornecedor, nome_cliente, endereco, status):
    dic = {
        'codigo': codigo,
        'fornecedor': fornecedor,
        'nome_cliente': nome_cliente,
        'endereco': endereco, 
        'status': status,
    }
    lista.append(dic)

    print("Sucesso")

def atualizar_status(codigo):
    for entrega in lista:
        if entrega['codigo'] == codigo:
            status = input("Informe o novo status: ")
            entrega['status'] = status
            print(f"\nCódigo: {entrega['codigo']}")
            print(f"Nome do fornecedor:: {entrega['fornecedor']}")
            print(f"Nome do cliente: {entrega['nome_cliente']}")
            print(f"Status (Pendente, Em andamento, Concluído): {entrega['status']}")

def buscar_entrega(codigo):
    for entrega in lista:
        if entrega['codigo'] == codigo:
            print(f"\nCódigo: {entrega['codigo']}")
            print(f"Nome do fornecedor:: {entrega['fornecedor']}")
            print(f"Nome do cliente: {entrega['nome_cliente']}")
            print(f"Endereço: {entrega['endereco']}")
            print(f"Status (Pendente, Em andamento, Concluído): {entrega['status']}")

def listar_entregas():
    for entrega in lista:
        print(f"\nCódigo: {entrega['codigo']}")
        print(f"Nome do fornecedor: {entrega['fornecedor']}")
        print(f"Nome do cliente: {entrega['nome_cliente']}")
        print(f"Endereço: {entrega['endereco']}")
        print(f"Status (Pendente, Em andamento, Concluído): {entrega['status']}")

def cont_entregas(fornecedor):
    soma_qtd = 0
    for entrega in lista:
        if entrega['fornecedor'] == fornecedor:
            soma_qtd += 1
    print(f"O fornecedor {entrega['fornecedor']} tem {soma_qtd} entregas cadastradas")

def menu():
    while True:
        print("-------------------------------------------------")
        print("1 - Cadastrar Entrega")
        print("2 - Atualizar o Status da Entrega")
        print("3 - Buscar de Entrega")
        print("4 - Listar Entregas")
        print("5 - Quantidade total de Entregas por fornecedor")
        print("-------------------------------------------------")
        opc = input("Informe uma opção: ")

        if opc == '1':
            codigo = input("Código: ")
            fornecedor = input("Nome do fornecedor: ")
            cliente  = input("Nome do cliente: ")
            endereco = input("Endereço: ")
            status = input("Status (Pendente, Em andamento, Concluído): ")
            cadastrar_entrega(codigo, fornecedor, cliente, endereco, status)
        elif opc == '2':
            codigo = input("Código: ")
            atualizar_status(codigo)
        elif opc == '3':
            codigo = input("Código: ")
            buscar_entrega(codigo)
        elif opc == '4':
            listar_entregas()
        elif opc == '5':
            fornecedor = input("Informe o nome do Fornecedor: ")
            cont_entregas(fornecedor)
menu()