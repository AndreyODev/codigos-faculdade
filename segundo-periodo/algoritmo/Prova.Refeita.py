lista_entregas = []
def cadastrar_entrega(codigo, fornecedor, cliente, endereco, status):
    dic_entregas = {
        "codigo": codigo,
        "fornecedor": fornecedor,
        "cliente": cliente,
        "endereco": endereco,
        "status": status
            }
    lista_entregas.append(dic_entregas)
    print("Cadastro feito com sucesso")
    
def atualizar_status(codigo):
    for entrega in lista_entregas:
        if entrega["codigo"] == codigo:
            atualizar = input("Informe o novo status: ")
            entrega["status"] = atualizar
            print("Status atualizado com sucesso")
        else:
            print("Entrega não encontrada")

def buscar_entrega(codigo):
    for entrega in lista_entregas:
        if entrega["codigo"] == codigo:
            print(entrega)
        else:
            print("A entrega não foi encontrada")


def listar_entregas(lista_entregas):
    if len(lista_entregas) > 0:
        for entrega in lista_entregas:
            print(f"Codigo: {entrega['codigo']}, Fornecedor: {entrega['fornecedor']}, Cliente: {entrega['cliente']}, Endereço: {entrega['endereco']}, Status: {entrega['status']}")
    else:
        print("Não há entrega disponível")
        
def contar_entregas_por_fornecedor(fornecedor):
    soma = 0
    for entrega in lista_entregas:
        if entrega["fornecedor"] == fornecedor:
            soma += 1
    print(f"O fornecedor {fornecedor} fez {soma} entregas")
            
def teste():
    cadastrar_entrega("E001", "Fornecedor A", "Cliente X", "Rua 1", "Pendente")
    cadastrar_entrega("E002", "Fornecedor b", "Cliente X", "Rua y", "Em andamento")
    cadastrar_entrega("E003", "Fornecedor A", "Cliente X", "Rua z", "Entregue")
def menu():
    while True:
        print("--------------------------------------------")
        print("Digite 1 para cadastrar uma nova entrega: ")
        print("Digite 2 para atualizar o status da entrega: ")
        print("Digite 3 para buscar uma entrega: ")
        print("Digite 4 para exibir todas as entregas: ")
        print("Digite 5 para visualizar o total de entregas cadastradas: ")
        print("Digite 6 para testar")
        print("Digite 7 para sair")
        print("--------------------------------------------")
        opc = input("Informe um número: ")
        if opc =="1":
            codigo = input("Informe o codigo: ")
            fornecedor = input("Informe o nome do fornecedor: ")
            cliente = input("Informe o nome do cliente: ")
            endereco = input("Informe o destino: ")
            status = input("Qual o status do inicial da entrega [Pendente, Em transito, Entregue]? ").lower()
            cadastrar_entrega(codigo, fornecedor, cliente, endereco, status)
        elif opc == "2":
            codigo = input("Informe o codigo para atualizar a entrega: ") 
            atualizar_status(codigo)
        elif opc == "3":
            codigo = input("Informe o codigo para buscar a entrega: ")
            buscar_entrega(codigo)
        elif opc == "4":
            listar_entregas(lista_entregas)
        elif opc == "5":
            fornecedor = input("Informe o nome do forneccedor para calcular o numero de entrega fornecido por ele: ")
            contar_entregas_por_fornecedor(fornecedor)
        elif opc =="6":
            teste()
        elif opc == "7":
            print("Saindo....")
            break
              
menu()